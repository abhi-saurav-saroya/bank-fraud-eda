import streamlit as st 

from components.multivariate.header import render as render_header
from components.multivariate.feature_selector import render as render_feature_selector


def render(df) -> None:
    """
    Render the Multivariate Analysis page.
    """
    
    render_header()

    st.divider()

    selected_features, target_feature = render_feature_selector(df)