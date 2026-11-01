"""
Pre-commit hook to validate the repository before a commit is allowed.

Two independent checks run on every commit:

1. Zola frontmatter validation for portfolio/software files. This ensures all
   .md files in content/portfolio/software (except _index.md) have the required
   frontmatter attributes.
2. Placeholder asset detection. Placeholder artwork is named with a token in the
   filename so that it can never be published by accident. While any placeholder
   file exists anywhere in the working tree, or any tracked text file still
   references one, commits are refused.

The placeholder check is deliberately repository-wide rather than limited to
staged files: a placeholder is a promise to replace it, and an unrelated commit
must not be the thing that quietly ships it.

To commit anyway (for example, to hand work-in-progress to another machine),
set ALLOW_PLACEHOLDERS=1 for that one commit:

    ALLOW_PLACEHOLDERS=1 git commit -m "wip: port redmond scaffold"
"""

import os
import re
import subprocess
import sys
import io

# Ensure UTF-8 output on Windows
if sys.platform == "win32":
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")

REQUIRED_ATTRIBUTES = [
    "title",
    "date",
    "description",
    "logo",
    "infobox_images",
    "application_category",
    "price_usd",
    "screenshot_urls",
    "operatingSystem",
    "release_notes",
    "programming_language",
    "development_environment",
    "license",
    "availability",
    "project_title",
    "aggregate_rating",
]

ATTRIBUTES_IN_EXTRA = [
    "logo",
    "infobox_images",
    "application_category",
    "price_usd",
    "screenshot_urls",
    "aggregate_rating",
]

SOFTWARE_DIR = "content/portfolio/software"

# Any file whose name contains this token is a stand-in for artwork that has not
# been produced yet. Keep the token loud and unlikely to occur by accident.
PLACEHOLDER_TOKEN = "__PLACEHOLDER__"

# Directories that never contain source material worth scanning.
SCAN_EXCLUDED_DIRS = {".git", "public", "node_modules", ".vscode"}

# The documentation describing the placeholder system names the token on
# purpose, and so does the workflow that guards against it. Neither is a
# reference to an actual asset.
REFERENCE_EXCLUDED_DIRS = SCAN_EXCLUDED_DIRS | {"docs", ".github"}

# File types that could carry a reference to a placeholder asset.
REFERENCE_FILE_SUFFIXES = (".md", ".html", ".css", ".js", ".toml", ".json", ".xml")

PLACEHOLDER_OVERRIDE_ENV = "ALLOW_PLACEHOLDERS"


def extract_frontmatter(filepath):
    """Extract frontmatter from a Zola markdown file."""
    try:
        with open(filepath, "r", encoding="utf-8") as f:
            content = f.read()
    except Exception as e:
        print(f"  [ERROR] Error reading file: {e}")
        return None

    # Extract content between +++ markers
    match = re.match(r"^\+\+\+\n(.*?)\n\+\+\+", content, re.DOTALL)
    if not match:
        print(f"  [ERROR] No valid frontmatter found")
        return None

    return match.group(1)


def validate_frontmatter(filepath, frontmatter):
    """Validate that all required attributes are present."""
    errors = []

    # Check top-level attributes
    for attr in ["title", "date", "description"]:
        if not re.search(rf'(#\s*)?{re.escape(attr)}\s*=', frontmatter):
            errors.append(attr)

    # Check for [taxonomies] section with required tags
    if "[taxonomies]" not in frontmatter:
        errors.append("[taxonomies]")
    else:
        # Match [taxonomies] and capture until next TOML section header or end
        taxonomies_match = re.search(r"\[taxonomies\](.*?)(?=\n\s*\[|\Z)", frontmatter, re.DOTALL)
        if taxonomies_match:
            taxonomies_section = taxonomies_match.group(1)
            # Check for software-categories
            if not re.search(r'(#\s*)?software-categories\s*=', taxonomies_section):
                errors.append("software-categories")
            # Check for programming-languages
            if not re.search(r'(#\s*)?programming-languages\s*=', taxonomies_section):
                errors.append("programming-languages")

    # Check for [extra] section
    if "[extra]" not in frontmatter:
        errors.extend(ATTRIBUTES_IN_EXTRA)
    else:
        # Extract from [extra] to the end
        extra_match = re.search(r"\[extra\](.*)", frontmatter, re.DOTALL)
        if extra_match:
            extra_section = extra_match.group(1)
            for attr in ATTRIBUTES_IN_EXTRA:
                if not re.search(
                    rf'(#\s*)?{re.escape(attr)}\s*=', extra_section
                ):
                    errors.append(attr)
        else:
            errors.extend(ATTRIBUTES_IN_EXTRA)

    # Check SEO attributes (can be anywhere in frontmatter)
    seo_attrs = [
        "operatingSystem",
        "release_notes",
        "programming_language",
        "development_environment",
        "license",
        "availability",
        "project_title",
        "questions",
    ]
    for attr in seo_attrs:
        if not re.search(rf'(#\s*)?{re.escape(attr)}\s*=', frontmatter):
            errors.append(attr)

    return errors


def get_staged_files():
    """Get list of staged .md files in portfolio/software directory."""
    try:
        result = subprocess.run(
            ["git", "diff", "--cached", "--name-only", "--diff-filter=ACM"],
            capture_output=True,
            text=True,
            check=True,
        )
        files = [
            f
            for f in result.stdout.strip().split("\n")
            if f.startswith(f"{SOFTWARE_DIR}/")
            and f.endswith(".md")
            and "_index.md" not in f
        ]
        return files
    except subprocess.CalledProcessError:
        return []


def find_placeholder_files():
    """Find every file in the working tree whose name marks it as a placeholder."""
    found = []

    for root, dirs, filenames in os.walk("."):
        dirs[:] = [d for d in dirs if d not in SCAN_EXCLUDED_DIRS]
        for filename in filenames:
            if PLACEHOLDER_TOKEN in filename:
                found.append(os.path.relpath(os.path.join(root, filename), "."))

    return sorted(found)


def find_placeholder_references():
    """Find source files that still point at a placeholder asset.

    A placeholder can be deleted while a template or markdown file keeps
    referencing it, which would ship a broken image instead of an obvious one.
    Both failure modes are worth blocking.
    """
    found = []

    for root, dirs, filenames in os.walk("."):
        dirs[:] = [d for d in dirs if d not in REFERENCE_EXCLUDED_DIRS]
        for filename in filenames:
            if not filename.endswith(REFERENCE_FILE_SUFFIXES):
                continue
            if PLACEHOLDER_TOKEN in filename:
                continue  # already reported as a placeholder file itself

            filepath = os.path.join(root, filename)
            try:
                with open(filepath, "r", encoding="utf-8") as f:
                    contents = f.read()
            except (OSError, UnicodeDecodeError):
                continue

            if PLACEHOLDER_TOKEN in contents:
                found.append(os.path.relpath(filepath, "."))

    return sorted(found)


def find_tracked_placeholders():
    """Placeholder files that git is actually tracking.

    This is the check that matters. An ignored file sitting on disk can never
    reach the history, but a tracked one is a single push away from being
    published, so this failure is never bypassable.
    """
    try:
        result = subprocess.run(
            ["git", "ls-files"], capture_output=True, text=True, check=True
        )
    except subprocess.CalledProcessError:
        return []

    return sorted(f for f in result.stdout.split("\n") if PLACEHOLDER_TOKEN in f)


def check_placeholders(pushing=False):
    """Refuse the commit while placeholder artwork is still in the repository."""
    tracked = find_tracked_placeholders()
    if tracked:
        print()
        print("[FAILED] Placeholder assets are tracked by git!")
        print()
        for filepath in tracked:
            print(f"    {filepath}")
        print()
        print("  These would enter the history and be published on the next push.")
        print("  Remove them from the index:  git rm --cached <file>")
        print("  They are covered by .gitignore, so this should not happen.")
        return 1

    # The override exists so work in progress can be handed between machines.
    # It deliberately does not apply to pushing, which is the point of no return.
    if os.environ.get(PLACEHOLDER_OVERRIDE_ENV) and not pushing:
        print(f"[SKIP] {PLACEHOLDER_OVERRIDE_ENV} is set, placeholder check bypassed")
        return 0

    placeholder_files = find_placeholder_files()
    placeholder_refs = find_placeholder_references()

    if not placeholder_files and not placeholder_refs:
        print("[OK] No placeholder assets found")
        return 0

    print()
    print("[FAILED] Placeholder assets are still present!")
    print()

    if placeholder_files:
        print("  Placeholder files:")
        for filepath in placeholder_files:
            print(f"    {filepath}")
        print()

    if placeholder_refs:
        print("  Files still referencing a placeholder:")
        for filepath in placeholder_refs:
            print(f"    {filepath}")
        print()

    print("  Replace them with the real artwork before committing.")
    print("  Asset requirements: docs/port-redmond-assets.md")
    if pushing:
        print("  There is no override when pushing. Finish the artwork first.")
    else:
        print(f"  To commit anyway: {PLACEHOLDER_OVERRIDE_ENV}=1 git commit ...")

    return 1


def check_frontmatter():
    """Validate frontmatter on staged portfolio/software pages."""
    files = get_staged_files()

    if not files:
        print("[OK] No portfolio/software files to validate")
        return 0

    total_errors = 0

    for filepath in files:
        if os.path.isfile(filepath):
            print(f"Validating: {filepath}")

            frontmatter = extract_frontmatter(filepath)
            if frontmatter is None:
                total_errors += 1
                continue

            errors = validate_frontmatter(filepath, frontmatter)
            if errors:
                for error in errors:
                    print(f"  [ERROR] Missing required attribute: {error}")
                total_errors += len(errors)

    if total_errors > 0:
        print()
        print("[FAILED] Frontmatter validation failed!")
        print("Please ensure all required frontmatter attributes are present.")
        return 1

    return 0


def main():
    """Run every check and report them all before failing."""
    pushing = "--pushing" in sys.argv

    # Both checks always run so a single attempt surfaces every problem rather
    # than making the author rediscover them one at a time.
    failures = check_frontmatter()
    failures += check_placeholders(pushing=pushing)

    if failures:
        return 1

    print()
    print("[OK] All validations passed!")
    return 0


if __name__ == "__main__":
    sys.exit(main())
