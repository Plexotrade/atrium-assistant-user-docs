#!/usr/bin/env python3

from pathlib import Path

# Repository root, assuming this script is inside the scripts directory.
ROOT_DIR = Path(__file__).resolve().parent.parent

# Directory containing Markdown documentation.
DOCS_DIR = ROOT_DIR / "docs"

SEPARATOR = "---"


def update_markdown_file(file_path: Path) -> bool:
    """Add a Markdown separator only if one is not already present."""
    content = file_path.read_text(encoding="utf-8")
    trimmed_content = content.rstrip()

    # Leave empty files unchanged.
    if not trimmed_content:
        return False

    # Skip files that already end with the separator.
    if trimmed_content.splitlines()[-1].strip() == SEPARATOR:
        return False

    # Add exactly one blank line before the separator.
    updated_content = f"{trimmed_content}\n\n{SEPARATOR}\n"

    file_path.write_text(updated_content, encoding="utf-8")
    return True


def main() -> None:
    if not DOCS_DIR.is_dir():
        raise SystemExit(f"Documentation directory not found: {DOCS_DIR}")

    updated_count = 0
    skipped_count = 0

    for file_path in sorted(DOCS_DIR.rglob("*.md")):
        if update_markdown_file(file_path):
            print(f"UPDATED: {file_path.relative_to(ROOT_DIR)}")
            updated_count += 1
        else:
            print(f"SKIPPED: {file_path.relative_to(ROOT_DIR)}")
            skipped_count += 1

    print("\nFinished.")
    print(f"Updated: {updated_count}")
    print(f"Skipped: {skipped_count}")


if __name__ == "__main__":
    main()
