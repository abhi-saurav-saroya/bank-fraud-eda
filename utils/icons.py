from pathlib import Path


ICON_DIR = Path("static/icons")


def get_svg(icon_name: str) -> str:
    """
    Returns SVG markup as a string.

    Example:
        get_svg("target")
    """

    path = ICON_DIR / f"{icon_name}.svg"

    if not path.exists():
        return ""

    return path.read_text(encoding="utf-8")