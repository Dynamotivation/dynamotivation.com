"""Checks data/releases.json before the site is built.

Run from the repository root: python scripts/validate_releases.py
Exits with status 1 and prints one line per problem when the file is invalid.
"""

import datetime
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
RELEASES = ROOT / "data" / "releases.json"
SOFTWARE = ROOT / "content" / "portfolio" / "software"
CATALOGS = ROOT / "content" / "v1" / "software"

VERSION = re.compile(r"^\d+\.\d+(\.\d+)?([-+][0-9A-Za-z.+-]+)?$")
DATE = re.compile(r"^\d{4}-\d{2}-\d{2}$")
ALLOWED_KEYS = {"version", "date", "highlights", "downloads"}
DOWNLOAD_KEYS = {"platform", "arch", "url", "sha256", "size"}
PLATFORMS = {
    "windows": {"x86", "x64", "arm64"},
    "macos": {"x64", "arm64"},
    "linux": {"x86", "x64", "arm64"},
}
SHA256 = re.compile(r"^[0-9a-f]{64}$")


def validate_downloads(at, downloads):
    if not isinstance(downloads, list):
        return [f"{at}: downloads must be a list"]
    errors = []
    seen = set()
    for index, download in enumerate(downloads):
        here = f"{at}.downloads[{index}]"
        if not isinstance(download, dict):
            errors.append(f"{here}: download must be an object")
            continue
        unknown = set(download) - DOWNLOAD_KEYS
        if unknown:
            errors.append(f"{here}: unknown keys {sorted(unknown)}")
        platform, arch = download.get("platform"), download.get("arch")
        if platform not in PLATFORMS or arch not in PLATFORMS.get(platform, ()):
            errors.append(f"{here}: unsupported platform/arch {platform!r}/{arch!r}")
        elif (platform, arch) in seen:
            errors.append(f"{here}: duplicate download for {platform}/{arch}")
        else:
            seen.add((platform, arch))
        url = download.get("url")
        if not isinstance(url, str) or not url.startswith("https://"):
            errors.append(f"{here}: url must be an https URL, got {url!r}")
        sha = download.get("sha256", "")
        if sha != "" and (not isinstance(sha, str) or not SHA256.match(sha)):
            errors.append(f"{here}: sha256 must be 64 lowercase hex characters")
        size = download.get("size", 0)
        if not isinstance(size, int) or isinstance(size, bool) or size < 0:
            errors.append(f"{here}: size must be a non-negative integer")
    return errors


HUB_TABLE = re.compile(r"^\[extra\.hub\][ \t]*\n(.*?)(?=^\[|\Z)", re.M | re.S)
EXPOSED = re.compile(r"^exposed\s*=\s*true\b", re.M)
SLUG_LINE = re.compile(r'^slug\s*=\s*"([^"]*)"', re.M)
PATH_LINE = re.compile(r'^path\s*=\s*"([^"]*)"', re.M)


def front_matter(path):
    """The raw TOML block. Zola reads TOML 1.1, which tomllib rejects, so match lines instead."""
    text = path.read_text(encoding="utf-8")
    return text.split("+++", 2)[1] if text.startswith("+++") else ""


def exposed_slugs():
    slugs = set()
    for page in SOFTWARE.glob("*.md"):
        table = HUB_TABLE.search(front_matter(page))
        if table and EXPOSED.search(table.group(1)):
            slugs.add(page.stem)
    return slugs


PAGE_DATE = re.compile(r"^date\s*=\s*(\d{4}-\d{2}-\d{2})", re.M)


def validate_page_dates(data):
    """A page's date is its first release; it must agree with the release data."""
    errors = []
    for slug, entry in data.items():
        page = SOFTWARE / f"{slug}.md"
        dated = [r["date"] for r in entry.get("releases", []) if isinstance(r, dict) and r.get("date")]
        match = PAGE_DATE.search(front_matter(page)) if page.is_file() else None
        if dated and match and match.group(1) != min(dated):
            errors.append(f"{slug}: page date {match.group(1)} is not its first release {min(dated)}")
    return errors


def validate_catalog_pages(data):
    """Every hub-exposed software needs a per-software release catalog page."""
    errors = []
    exposed = exposed_slugs()
    for slug in sorted(exposed):
        stub = CATALOGS / f"{slug}.md"
        if not stub.is_file():
            errors.append(f"{slug}: exposed to the hub but has no content/v1/software/{slug}.md")
            continue
        front = front_matter(stub)
        expected = f"v1/software/{slug}/releases.json"
        path, stub_slug = PATH_LINE.search(front), SLUG_LINE.search(front)
        if not path or path.group(1) != expected or not stub_slug or stub_slug.group(1) != slug:
            errors.append(f'{slug}: {stub.name} must set path = "{expected}" and extra.slug = "{slug}"')
    for stub in CATALOGS.glob("*.md"):
        if stub.name != "_index.md" and stub.stem not in exposed:
            errors.append(f"{stub.stem}: release catalog page for software that is not exposed to the hub")
    return errors


def validate(data):
    errors = []
    if not isinstance(data, dict):
        return ["top level must be an object keyed by page slug"]

    for slug, entry in data.items():
        where = f"{slug}"
        if not (SOFTWARE / f"{slug}.md").is_file():
            errors.append(f"{where}: no content/portfolio/software/{slug}.md")
        if not isinstance(entry, dict) or set(entry) != {"releases"}:
            errors.append(f'{where}: expected exactly one key, "releases"')
            continue
        releases = entry["releases"]
        if not isinstance(releases, list):
            errors.append(f"{where}: releases must be a list")
            continue

        seen = set()
        previous = None
        for index, release in enumerate(releases):
            at = f"{where}[{index}]"
            if not isinstance(release, dict):
                errors.append(f"{at}: release must be an object")
                continue
            unknown = set(release) - ALLOWED_KEYS
            if unknown:
                errors.append(f"{at}: unknown keys {sorted(unknown)}")

            version = release.get("version")
            if not isinstance(version, str) or not VERSION.match(version):
                errors.append(f"{at}: version must look like 1.2 or 1.2.3, got {version!r}")
            elif version in seen:
                errors.append(f"{at}: duplicate version {version}")
            else:
                seen.add(version)

            date = release.get("date", "")
            if date != "":
                if not isinstance(date, str) or not DATE.match(date):
                    errors.append(f"{at}: date must be YYYY-MM-DD, got {date!r}")
                else:
                    try:
                        parsed = datetime.date.fromisoformat(date)
                    except ValueError:
                        errors.append(f"{at}: not a real date: {date}")
                    else:
                        if previous is not None and parsed > previous:
                            errors.append(f"{at}: releases must be newest first ({date} is after the release before it)")
                        previous = parsed

            if "downloads" in release:
                errors.extend(validate_downloads(at, release["downloads"]))

            highlights = release.get("highlights", [])
            if not isinstance(highlights, list) or not all(
                isinstance(h, str) and h.strip() for h in highlights
            ):
                errors.append(f"{at}: highlights must be a list of non-empty strings")
    return errors


def main():
    try:
        data = json.loads(RELEASES.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as error:
        print(f"{RELEASES}: {error}")
        return 1
    errors = validate(data) + validate_catalog_pages(data) + validate_page_dates(data)
    for error in errors:
        print(error)
    if errors:
        return 1
    print(f"releases.json OK ({len(data)} pages)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
