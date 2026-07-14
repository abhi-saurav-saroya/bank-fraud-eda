import streamlit as st

from utils.feature_config import get_feature_groups


DEFAULT_FEATURES = [
    "transaction_amount",
    "credit_score",
    "distance_from_home_km",
    "account_balance",
]


def render(df):
    """
    Render feature selector for multivariate analysis.
    """

    st.markdown(
        f'<div class="section"> <h2 class="section-title"> Feature Selection </h2> <div class="section-subtitle"> Select multiple features to analyse simultaneously against the target variable. </div> </div>',
        unsafe_allow_html=True,
    )

    feature_groups = get_feature_groups(df)

    numerical_features = feature_groups["Numerical"]
    binary_features = feature_groups["Binary"]

    binary_features.remove("is_fraud")

    available_features = numerical_features + binary_features

    c1, c2 = st.columns([3, 0.5])

    with c1:
        selected_features = st.multiselect(
            label="Select Features",
            options=available_features,
            default=DEFAULT_FEATURES,
            max_selections=6,
            placeholder="Choose up to 6 features...",
        )

    with c2:
        st.text_input(
            label="Target Variable",
            value="is_fraud",
            disabled=True,
        )

    if len(selected_features) < 2:
        st.info(
            "Please select at least two features."
        )
        st.stop()

    return selected_features, "is_fraud"