import streamlit as st

from utils.feature_config import (
    get_binary_columns,
    get_categorical_columns,
    get_numeric_columns,
)


def render(df) -> tuple:
    """
    Render variable selector for bivariate analysis.
    """

    st.markdown(
        f'<div class="section"> <h2 class="section-title"> Variable Selection </h2> <div class="section-subtitle"> Select any two features to explore their relationship. </div> </div>',
        unsafe_allow_html=True,
    )

    numeric = get_numeric_columns(df)
    categorical = get_categorical_columns(df)
    binary = get_binary_columns(df)

    feature_types = {}

    for col in numeric:
        feature_types[col] = "Numerical"

    for col in categorical:
        feature_types[col] = "Categorical"

    for col in binary:
        feature_types[col] = "Binary"

    all_features = (
        numeric
        + categorical
        + binary
    )

    col1, col2 = st.columns(2)

    with col1:
        x_feature = st.selectbox(
            "X-axis Feature",
            options=all_features,
            index=0,
        )

    with col2:
        default_index = (
            1
            if len(all_features) > 1
            else 0
        )

        y_feature = st.selectbox(
            "Y-axis Feature",
            options=all_features,
            index=default_index,
        )

    x_type = feature_types[x_feature]
    y_type = feature_types[y_feature]

    return (
        x_feature,
        y_feature,
        x_type,
        y_type,
    )