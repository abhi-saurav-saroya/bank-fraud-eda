import pandas as pd
import plotly.express as px
import streamlit as st

from plots.theme import COLORS, apply_theme

from utils.icons import get_svg

pin_icon = get_svg("pin")
check_icon = get_svg("check")


def create_pie_chart(df: pd.DataFrame, title: str):
    """
    Create donut chart showing legitimate vs fraudulent transactions.
    """

    color_map = {
        "Legitimate": "#10B981",
        "Fraudulent": "#EF4444",
    }

    fig = px.pie(
        df,
        names="Transaction",
        values="Count",
        hole=0.65,
        color="Transaction",
        color_discrete_map=color_map,
    )

    fig.update_traces(
        textinfo="percent+label",
        hovertemplate=(
            "<b>%{label}</b>"
            "<br>Transactions: %{value}"
            "<br>%{percent}"
            "<extra></extra>"
        ),
        hoverlabel=dict(
            bgcolor="white",
            font=dict(color="#000000"),
        ),
    )

    fig.update_layout(
        title=title,
        showlegend=False,
    )

    return apply_theme(fig)


def render(df: pd.DataFrame):
    """
    Render PIN change fraud insight.
    """

    st.markdown(
        f'<div class="section"> <h2 class="section-title"> Impact of Recent PIN Changes on Fraud Risk </h2> <div class="section-subtitle"> Compare fraud rates between accounts with recently changed PINs and accounts with unchanged PINs. The accompanying distribution charts provide additional context about the composition of legitimate and fraudulent transactions. </div> </div>',
        unsafe_allow_html=True,
    )

    fraud_rate = (
        df.groupby("pin_changed_recently")["is_fraud"]
        .mean()
        .mul(100)
        .reset_index()
    )

    fraud_rate["PIN Status"] = fraud_rate["pin_changed_recently"].map(
        {
            0: "Unchanged",
            1: "Changed",
        }
    )

    fraud_rate.rename(
        columns={
            "is_fraud": "Fraud Rate (%)",
        },
        inplace=True,
    )

    unchanged = (
        df[df["pin_changed_recently"] == 0]["is_fraud"]
        .value_counts()
        .rename(
            index={
                0: "Legitimate",
                1: "Fraudulent",
            }
        )
        .reset_index()
    )

    unchanged.columns = [
        "Transaction",
        "Count",
    ]

    changed = (
        df[df["pin_changed_recently"] == 1]["is_fraud"]
        .value_counts()
        .rename(
            index={
                0: "Legitimate",
                1: "Fraudulent",
            }
        )
        .reset_index()
    )

    changed.columns = [
        "Transaction",
        "Count",
    ]

    left, right = st.columns(2)
    with left:
        st.plotly_chart(
            create_pie_chart(
                unchanged,
                "PIN Unchanged",
            ),
            width="stretch",
        )

    with right:
        st.plotly_chart(
            create_pie_chart(
                changed,
                "PIN Changed",
            ),
            width="stretch",
        )

    highest = fraud_rate.loc[
        fraud_rate["Fraud Rate (%)"].idxmax()
    ]

    lowest = fraud_rate.loc[
        fraud_rate["Fraud Rate (%)"].idxmin()
    ]

    difference = (
        highest["Fraud Rate (%)"]
        - lowest["Fraud Rate (%)"]
    )

    
    insights = []

    insights.append(
        f'Accounts with a <b>{highest["PIN Status"]}</b> PIN recorded the higher fraud rate of <b>{highest["Fraud Rate (%)"]:.2f}%</b>.'
    )

    insights.append(
        f"The fraud rate for accounts with an <b>{lowest["PIN Status"]}</b> PIN was <b>{lowest["Fraud Rate (%)"]:.2f}%</b>."
    )

    insights.append(
        f"This represents a difference of <b>{difference:.2f} percentage points</b> between the two groups."
    )

    insights.append(
        f"The donut charts show that legitimate transactions remain the majority in both groups, while the proportion of fraudulent transactions differs noticeably between recently changed and unchanged PINs."
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