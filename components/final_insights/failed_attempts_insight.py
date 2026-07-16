import pandas as pd
import streamlit as st

from plots.line_chart import create as create_line_chart

from utils.icons import get_svg

pin_icon = get_svg("pin")
check_icon = get_svg("check")


def render(df):
    """
    Render fraud rate by failed authentication attempts.
    """

    st.markdown(
        f'<div class="section"> <h2 class="section-title"> Impact of Failed Authentication Attempts on Fraud Risk </h2> <div class="section-subtitle"> Examine how the fraud rate changes as the number of failed authentication attempts increases. This helps identify whether repeated authentication failures are a meaningful fraud indicator. </div> </div>',
        unsafe_allow_html=True,
    )
    

    fraud_rate = (
        df.groupby("failed_attempts")["is_fraud"]
        .mean()
        .mul(100)
        .reset_index()
    )

    fraud_rate.columns = [
        "Failed Attempts",
        "Fraud Rate (%)",
    ]

    fig = create_line_chart(
        df=fraud_rate,
        x="Failed Attempts",
        y="Fraud Rate (%)",
        markers=True,
        title="Fraud Rate by Failed Authentication Attempts",
    )

    st.plotly_chart(
        fig,
        width="stretch",
    )

    highest_row = fraud_rate.loc[
        fraud_rate["Fraud Rate (%)"].idxmax()
    ]

    lowest_row = fraud_rate.loc[
        fraud_rate["Fraud Rate (%)"].idxmin()
    ]

    increase = highest_row["Fraud Rate (%)"] - lowest_row["Fraud Rate (%)"]

    trend = fraud_rate["Fraud Rate (%)"].is_monotonic_increasing

    trend_text = (
        "The fraud rate increases consistently as authentication failures increase."
        if trend
        else
        "The fraud rate generally increases with additional authentication failures, although minor fluctuations are present."
    )

    insights = []

    insights.append(
        f"Accounts with <b>{int(highest_row["Failed Attempts"])}</b> failed authentication attempt(s) recorded the highest fraud rate of <b>{highest_row["Fraud Rate (%)"]:.2f}%</b>."
    )

    insights.append(
        f"Transactions with <b>{int(lowest_row["Failed Attempts"])}</b> failed authentication attempt(s) showed the lowest fraud rate of <b>{lowest_row["Fraud Rate (%)"]:.2f}%</b>."
    )

    insights.append(
        f"The difference between the lowest and highest observed fraud rates is <b>{increase:.2f} percentage points</b>."
    )

    insights.append(
        trend_text
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