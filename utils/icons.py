from pathlib import Path


ICON_DIRECTORY = Path("../static/icons")


def load_svg(filename: str, width: int = 24, height: int = 24, css_class: str = "") -> str:
    """
    Returns an inline SVG with custom size.
    """

    icon_path = ICON_DIRECTORY / filename

    if not icon_path.exists():
        raise FileNotFoundError(
            f"Icon not found: {filename}"
        )

    svg = icon_path.read_text(encoding="utf-8")

    svg = svg.replace(
        "<svg",
        f'<svg class="{css_class}" width="{width}" height="{height}"'
    )

    return svg