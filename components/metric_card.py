import streamlit as st


def render(*, icon: str, value, label: str,) -> None:
    """
    Render a reusable metric card.
    """

    st.markdown(
        f'<div class="metric-card"> <div class="metric-icon"> {icon} </div> <div class="metric-value"> {value} </div> <div class="metric-label"> {label} </div> </div>',
        unsafe_allow_html=True,
    )