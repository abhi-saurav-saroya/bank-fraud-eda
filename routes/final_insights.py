import streamlit as st 

from components.final_insights.header import render as render_header

def render(df) -> None:
    """
    Render the Final Insights page.
    """

    render_header()

    st.divider()