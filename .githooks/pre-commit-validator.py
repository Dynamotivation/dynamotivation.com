"""
Pre-commit hook to validate Zola frontmatter in portfolio/software files.
This script ensures all .md files in content/portfolio/software (except _index.md)
have the required frontmatter attributes.
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
    "release_notes",
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
        "release_notes",
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


def main():
    """Main entry point."""
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
        print("[FAILED] Pre-commit validation failed!")
        print("Please ensure all required frontmatter attributes are present.")
        return 1
    else:
        print()
        print("[OK] All validations passed!")
        return 0


if __name__ == "__main__":
    sys.exit(main())
