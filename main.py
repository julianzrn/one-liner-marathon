"""Entry for make.fun's "One-Liner Marathon".

Running this program writes the entry text to /output/entry.txt.
"""

from pathlib import Path

SETUP = "My therapist says I should stop bottling things up, which is rich coming from a woman "
SCENE = "whose waiting room has twelve chairs, one plant, "
TAG = "and forty years of other people's unsaid things in the wallpaper."

ENTRY = SETUP + SCENE + TAG

OUTPUT_PATH = Path("/output/entry.txt")


def write_entry(path: Path = OUTPUT_PATH) -> None:
    """Write the entry text to the output file, with no trailing newline."""
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(ENTRY, encoding="utf-8")


if __name__ == "__main__":
    write_entry()
