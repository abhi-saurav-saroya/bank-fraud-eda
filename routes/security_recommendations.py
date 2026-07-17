import streamlit as st

from components.security_recommendations.header import render as render_header

def render(df) -> None:
    """
    Render the Security Recommendations page.
    """

    render_header()