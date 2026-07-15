import pandas as pd
import streamlit as st

from plots.horizontal_bar_chart import create as create_horizontal_bar_chart


def render(df):
    """
    Render correlation of numerical features with fraud.
    """

    st.markdown(
        f'<div class="section"> <h2 class="section-title"> Correlation of Numerical Features with Fraud </h2> <div class="section-subtitle"> Measure how strongly each numerical feature is linearly associated with fraudulent transactions. </div> </div>',
        unsafe_allow_html=True,
    )

    numerical = (
        df.select_dtypes(include="number")
        .drop(columns=["is_fraud"])
    )

    correlations = (
        numerical
        .corrwith(df["is_fraud"])
        .sort_values()
    )

    feature_labels = {
        feature: feature.replace("_", " ").title()
        for feature in correlations.index
    }

    plot_df = pd.DataFrame(
        {
            "Feature": correlations.index.map(feature_labels),
            "Correlation": correlations.values,
        }
    )

    fig = create_horizontal_bar_chart(
        data=plot_df,
        x="Correlation",
        y="Feature",
        title="Correlation with Fraud",
    )

    st.plotly_chart(
        fig,
        width="stretch",
    )