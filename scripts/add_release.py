"""Records a new release in data/releases.json.

Run from the repository root by the All-Out-Attack-Generator-Source release
workflow, or by hand:

    python scripts/add_release.py --slug all-out-attack-generator --version 1.2.3 \
        --date 2026-11-01 --highlights-file notes.txt \
        --download windows x86 https://example.com/setup.exe <sha256> <size>

Existing releases are kept untouched. The new release becomes the newest entry.
Running it again for a version that is already recorded replaces that entry in
place, so a retried workflow run is harmless. The file is validated before it
is written; on any problem nothing is changed and the exit status is 1.
"""

import argparse
import json
import sys
from pathlib import Path

from validate_releases import RELEASES, SOFTWARE, validate


def parse_args(argv):
    parser = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    parser.add_argument("--slug", required=True, help="software page slug")
    parser.add_argument("--version", required=True)
    parser.add_argument("--date", required=True, help="YYYY-MM-DD")
    parser.add_argument("--highlights-file", required=True, help="one highlight per line; blank lines and leading '-'/'*' bullets are ignored")
    parser.add_argument(
        "--download",
        nargs=5,
        action="append",
        default=[],
        metavar=("PLATFORM", "ARCH", "URL", "SHA256", "SIZE"),
    )
    return parser.parse_args(argv)


def read_highlights(path):
    lines = Path(path).read_text(encoding="utf-8").splitlines()
    return [line.strip().lstrip("-*").strip() for line in lines if line.strip().lstrip("-*").strip()]


def main(argv):
    args = parse_args(argv)
    if not (SOFTWARE / f"{args.slug}.md").is_file():
        print(f"no content/portfolio/software/{args.slug}.md")
        return 1

    data = json.loads(RELEASES.read_text(encoding="utf-8"))
    releases = data.setdefault(args.slug, {"releases": []})["releases"]

    release = {
        "version": args.version,
        "date": args.date,
        "highlights": read_highlights(args.highlights_file),
        "downloads": [
            {"platform": p, "arch": a, "url": u, "sha256": h.lower(), "size": int(s)}
            for p, a, u, h, s in args.download
        ],
    }
    for index, existing in enumerate(releases):
        if existing["version"] == args.version:
            releases[index] = release
            break
    else:
        releases.insert(0, release)

    errors = validate(data)
    if errors:
        print("\n".join(errors))
        return 1
    with RELEASES.open("w", encoding="utf-8", newline="\n") as out:
        out.write(json.dumps(data, indent=2, ensure_ascii=False) + "\n")
    print(f"recorded {args.slug} {args.version} ({len(releases)} releases)")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
