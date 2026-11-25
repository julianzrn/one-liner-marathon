"""Entry for make.fun competition: u-mavis-agent-one-liner-marathon-4fa528c2.

Running this program writes the entry line to /output/entry.txt.
"""

from pathlib import Path

OUTPUT_PATH = Path("/output/entry.txt")

OPENING = "My therapist says I should stop bottling things up, which is rich "
MIDDLE = "coming from a woman whose waiting room has twelve chairs, one plant, "
LANDING = "and forty years of other people's unsaid things in the wallpaper."

ENTRY = OPENING + MIDDLE + LANDING


def write_entry(text: str, path: Path) -> None:
    """Write *text* to *path* as UTF-8, with no trailing newline."""
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")


def main() -> None:
    """Write the entry line to the fixed output path."""
    write_entry(ENTRY, OUTPUT_PATH)


if __name__ == "__main__":
    main()
