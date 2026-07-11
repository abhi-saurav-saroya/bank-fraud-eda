import streamlit as st

from utils.feature_config import get_feature_groups


def render(df) -> tuple:
    """
    Render the feature selector.
    """

    feature_groups = get_feature_groups(df)

    st.markdown(
        f'<div class="section"> <h2 class="section-title"> Feature Selection </h2> <div class="section-subtitle"> Select a feature category and explore its distribution, statistics and insights. </div> </div>',
        unsafe_allow_html=True,
    )

    left, right = st.columns([1, 2])

    with left:

        feature_type = st.radio(
            label="Feature Type",
            options=[
                "Numerical",
                "Categorical",
                "Binary",
            ],
            horizontal=False,
        )

    with right:

        feature = st.selectbox(
            "Feature",
            feature_groups[feature_type],
        )

    return feature_type, feature