import pandas as pd
import streamlit as st

from plots.horizontal_bar_chart import create as create_horizontal_bar_chart

from utils.icons import get_svg

pin_icon = get_svg("pin")
check_icon = get_svg("check")


def render(df):
    """
    Correlation of numerical features with fraud.
    """

    st.markdown(
        f'<div class="section"> <h2 class="section-title"> Correlation of Numerical Features with Fraud </h2> <div class="section-subtitle"> Pearson correlation coefficients between numerical variables and the fraud indicator. Larger absolute values indicate stronger linear relationships with fraudulent transactions. </div> </div>',
        unsafe_allow_html=True,
    )
    numerical = (
        df.select_dtypes(include="number")
        .drop(columns=["is_fraud"])
    )

    fraud_corr = (
        numerical
        .corrwith(df["is_fraud"])
        .sort_values()
    )

    feature_labels = {
        column: column.replace("_", " ").title()
        for column in fraud_corr.index
    }

    plot_df = pd.DataFrame(
        {
            "Feature": fraud_corr.index.map(feature_labels),
            "Correlation": fraud_corr.values,
        }
    )

    fig = create_horizontal_bar_chart(
        data=plot_df,
        x="Correlation",
        y="Feature",
        title="Correlation of Numerical Features with Fraud",
    )

    st.plotly_chart(
        fig,
        width="stretch",
    )

    strongest_positive = fraud_corr.idxmax()
    strongest_negative = fraud_corr.idxmin()

    strongest_positive_value = fraud_corr.max()
    strongest_negative_value = fraud_corr.min()

    insights = []

    insights.append(
        f"<b>{feature_labels[strongest_positive]}</b> has the strongest positive correlation with fraud (<b>{strongest_positive_value:.3f}</b>), indicating that higher values of this feature are more frequently associated with fraudulent transactions."
    )

    insights.append(
        f"<b>{feature_labels[strongest_negative]}</b> shows the strongest negative correlation (<b>{strongest_negative_value:.3f}</b>), suggesting that larger values are generally associated with legitimate transactions."
    )

    insights.append(
        f"Most variables exhibit relatively weak individual correlations, suggesting that fraud detection benefits from combining multiple features rather than relying on a single predictor."
    )

    items = ""
    for insight in insights:
        items += (
            f"<li>{check_icon}"
            f"<span>{insight}</span></li>"
        )

    st.markdown(
        f'<div class="insight-card"> <div class="insight-heading"> {pin_icon} Key Findings </div> <ul class="insight-list"> {items} </ul>',
        unsafe_allow_html=True,
    )