import streamlit as st

from components.dataset_header import render as render_dataset_header
from components.dataset_preview import render as render_dataset_preview
from components.column_explorer import render as render_column_explorer
# from components.feature_summary import render as render_feature_summary


def render(raw_df, clean_df):
    """
    Render Dataset Explorer page.
    """

    render_dataset_header(raw_df, clean_df)

    st.markdown("<br>", unsafe_allow_html=True)

    render_dataset_preview(raw_df, clean_df)

    st.markdown("<br>", unsafe_allow_html=True)

    render_column_explorer(clean_df)

    st.markdown("<br>", unsafe_allow_html=True)

    # render_feature_summary(clean_df)