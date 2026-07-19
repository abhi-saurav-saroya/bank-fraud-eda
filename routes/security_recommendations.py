import streamlit as st

from components.security_recommendations.header import render as render_header
from components.security_recommendations.time_based_detection import render as render_time_based_detection

def render() -> None:
    """
    Render the Security Recommendations page.
    """

    render_header()

    st.divider()

    render_time_based_detection()