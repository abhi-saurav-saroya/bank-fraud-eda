import streamlit as st
import plotly.express as px

from utils.icons import get_svg

from plots.theme import COLORS, apply_theme

pin_icon = get_svg("pin")
check_icon = get_svg("check")

def create(df, x, y, title=None, color=None,):
    """
    Create a comparison bar chart for aggregated values.
    """

    fig = px.bar(
        df,
        x=x,
        y=y,
        color=color if color else x,
        color_discrete_sequence=COLORS,
        text_auto=".2f",
    )

    fig.update_traces(
        hovertemplate=(
            "<b>%{x}</b>"
            "<br>%{y:.2f}"
            "<extra></extra>"
        ),
        hoverlabel=dict(
            bgcolor="white",
            font=dict(color="#000000"),
        ),
        textposition="outside",
    )

    fig.update_layout(
        title=title,
        showlegend=color is not None,
        xaxis_title=x.replace("_", " ").title(),
        yaxis_title=y.replace("_", " ").title(),
        uniformtext_minsize=10,
        uniformtext_mode="hide",
    )

    return apply_theme(fig)

def render(df):
    """
    Render fraud rate for domestic vs international transactions.
    """

    st.markdown(
        f'<div class="section"> <h2 class="section-title"> Domestic vs International Transaction Risk </h2> <div class="section-subtitle"> Compare fraud rates between domestic and international transactions to determine whether cross-border payments represent a higher fraud risk. </div> </div>',
        unsafe_allow_html=True,
    )

    international_fraud_rate = (
        df.groupby("is_international")["is_fraud"]
          .mean()
          .mul(100)
          .reset_index()
    )

    international_fraud_rate["Transaction Type"] = (
        international_fraud_rate["is_international"]
        .map({
            0: "Domestic",
            1: "International"
        })
    )

    international_fraud_rate.rename(
        columns={
            "is_fraud": "Fraud Rate (%)"
        },
        inplace=True,
    )

    fig = create(
        df=international_fraud_rate,
        x="Transaction Type",
        y="Fraud Rate (%)",
        title="Fraud Rate: Domestic vs International Transactions",
    )

    st.plotly_chart(
        fig,
        width="stretch",
    )
    

    domestic = international_fraud_rate.loc[
        international_fraud_rate["Transaction Type"] == "Domestic",
        "Fraud Rate (%)",
    ].iloc[0]

    international = international_fraud_rate.loc[
        international_fraud_rate["Transaction Type"] == "International",
        "Fraud Rate (%)",
    ].iloc[0]

    difference = international - domestic

    ratio = (
        international / domestic
        if domestic > 0
        else 0
    )

    riskier = (
        "International"
        if international > domestic
        else "Domestic"
    )

    insights = []

    insights.append(
        f"<b>{riskier}</b> transactions recorded the higher fraud rate."
    )

    insights.append(
        f"Domestic transactions showed a fraud rate of <b>{domestic:.2f}%</b>, whereas international transactions recorded <b>{international:.2f}%</b>."
    )

    insights.append(
        f"The difference between the two categories is <b>{difference:.2f} percentage points</b>."
    )

    insights.append(
        f"International transactions are approximately <b>{ratio:.2f}</b> times more likely to be fraudulent than domestic transactions."
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