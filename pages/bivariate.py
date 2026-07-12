import streamlit as st

from components.bivariate.header import render as render_header
from components.bivariate.variable_selector import render as render_variable_selector

def render(df):
    """
    Render the Bivariate Analysis page.
    """
    
    render_header()

    st.markdown("<br>", unsafe_allow_html=True)

    render_variable_selector(df)