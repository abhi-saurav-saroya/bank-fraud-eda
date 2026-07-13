import streamlit as st 

from components.multivariate.header import render as render_header


def render(df) -> None:
    """
    Render the Multivariate Analysis page.
    """
    
    render_header()

    st.divider()