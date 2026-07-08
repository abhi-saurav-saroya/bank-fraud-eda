from pathlib import Path

import streamlit as st


CSS_DIRECTORY = Path("static/css")


def load_css() -> None:
    """
    Loads every CSS file inside static/css
    in alphabetical order.
    """

    if not CSS_DIRECTORY.exists():
        raise FileNotFoundError(
            f"CSS directory not found: {CSS_DIRECTORY}"
        )

    css = ""

    for file in sorted(CSS_DIRECTORY.glob("*.css")):
        css += file.read_text(encoding="utf-8")
        css += "\n"

    st.markdown(
        f"<style>{css}</style>",
        unsafe_allow_html=True,
    )