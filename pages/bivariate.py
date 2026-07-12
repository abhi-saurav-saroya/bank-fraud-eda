import streamlit as st

from components.bivariate.header import render as render_header

def render(df):
    """
    Render the Bivariate Analysis page.
    """
    
    render_header()

    st.markdown("<br>", unsafe_allow_html=True)