import streamlit as st 

from components.final_insights.header import render as render_header
from components.final_insights.correlation_with_fraud import render as render_correlation_with_fraud

def render(df) -> None:
    """
    Render the Final Insights page.
    """

    render_header()

    st.divider()

    render_correlation_with_fraud(df)