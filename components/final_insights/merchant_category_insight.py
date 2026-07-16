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
    Render fraud rate by merchant category.
    """

    st.markdown(
        f'<div class="section"> <h2 class="section-title"> Fraud Risk Across Merchant Categories </h2> <div class="section-subtitle"> Compare fraud rates across merchant categories to identify business sectors that experience a disproportionately high number of fraudulent transactions. </div> </div>',
        unsafe_allow_html=True,
    )
    

    merchant_fraud_rate = (
        df.groupby("merchant_category")["is_fraud"]
        .mean()
        .mul(100)
        .sort_values(ascending=False)
        .reset_index()
    )

    merchant_fraud_rate.columns = [
        "Merchant Category",
        "Fraud Rate (%)",
    ]

    fig = create(
        df=merchant_fraud_rate,
        x="Merchant Category",
        y="Fraud Rate (%)",
        title="Fraud Rate by Merchant Category",
    )

    fig.update_layout(
        xaxis_tickangle=-45,
    )

    st.plotly_chart(
        fig,
        width="stretch",
    )


    highest = merchant_fraud_rate.iloc[0]
    lowest = merchant_fraud_rate.iloc[-1]

    average = merchant_fraud_rate["Fraud Rate (%)"].mean()

    above_average = merchant_fraud_rate[
        merchant_fraud_rate["Fraud Rate (%)"] > average
    ]["Merchant Category"].tolist()

    categories = ", ".join(above_average)

    insights = []

    insights.append(
        f'<b>{highest["Merchant Category"]}</b> recorded the highest fraud rate at <b>{highest["Fraud Rate (%)"]:.2f}%</b>.'
    )

    insights.append(
        f"<b>{lowest["Merchant Category"]}</b> recorded the lowest fraud rate at <b>{lowest["Fraud Rate (%)"]:.2f}%</b>."
    )

    insights.append(
        f"The difference between the highest and lowest fraud-risk merchant categories is <b>{highest["Fraud Rate (%)"] - lowest["Fraud Rate (%)"]:.2f} percentage points</b>."
    )

    insights.append(
        f"Merchant categories with fraud rates above the overall average include: <b>{categories}</b>."
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