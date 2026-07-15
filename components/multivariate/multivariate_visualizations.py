import streamlit as st

from plots.correlation_heatmap import create as create_correlation_heatmap
from plots.scatter_matrix import create as create_scatter_matrix

from utils.feature_config import get_feature_groups


def render(df, selected_features, target):
    """
    Render multivariate visualizations.
    """

    st.markdown(
        f'<div class="section"> <h2 class="section-title"> Multivariate Visualizations </h2> <div class="section-subtitle"> Compare the selected features simultaneously against the fraud target using multiple visualization techniques. </div> </div>',
        unsafe_allow_html=True,
    )

    groups = get_feature_groups(df)

    numeric_features = groups["Numerical"] + groups["Discrete Numerical"]

    numeric_features = [
        feature
        for feature in selected_features
        if feature in numeric_features
    ]

    if len(numeric_features) < 2:
        st.warning(
            "Please select at least two numerical or discrete numerical features."
        )
        return

    heatmap = create_correlation_heatmap(
        df=df,
        columns=numeric_features,
    )
    st.plotly_chart(
        heatmap,
        width="stretch",
    )

    st.markdown("<br>", unsafe_allow_html=True)


    scatter = create_scatter_matrix(
        df=df,
        features=numeric_features,
        target=target,
    )
    st.plotly_chart(
        scatter,
        width="stretch",
    )