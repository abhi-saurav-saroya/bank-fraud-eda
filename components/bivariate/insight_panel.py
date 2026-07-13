import pandas as pd
import streamlit as st

from utils.icons import get_svg


panel_icon = get_svg("lightbulb")
check_icon = get_svg("check")


def render(df: pd.DataFrame, x_feature: str, y_feature: str, x_type: str, y_type: str):
    """
    Render automatic insights for the selected relationship.
    """

    st.markdown(
        f'<div class="section"> <h2 class="section-title">Key Insights</h2> <div class="section-subtitle"> Automatically generated observations describing the selected relationship. </div> </div>',
        unsafe_allow_html=True,
    )

    insights = []


    if x_type == "Numerical" and y_type == "Numerical":

        corr = df[x_feature].corr(df[y_feature])

        if abs(corr) < 0.20:
            strength = "very weak"
        elif abs(corr) < 0.40:
            strength = "weak"
        elif abs(corr) < 0.60:
            strength = "moderate"
        elif abs(corr) < 0.80:
            strength = "strong"
        else:
            strength = "very strong"

        direction = (
            "positive"
            if corr >= 0
            else "negative"
        )

        insights.append(
            f"The correlation coefficient is {corr:.3f}, indicating a {strength} {direction} relationship."
        )

        insights.append(
            f"The dataset contains {len(df):,} observations for this comparison."
        )

        missing = (
            df[[x_feature, y_feature]]
            .isna()
            .sum()
            .sum()
        )

        if missing == 0:
            insights.append(
                "No missing values are present in either feature."
            )
        else:
            insights.append(
                f"There are {missing} missing values across the selected variables."
            )

        if abs(corr) >= 0.7:
            insights.append(
                "The two variables exhibit a strong linear association."
            )
        elif abs(corr) <= 0.2:
            insights.append(
                "Little evidence of a linear relationship is observed."
            )


    elif ( (x_type == "Numerical" and y_type != "Numerical") or (y_type == "Numerical" and x_type != "Numerical") ):

        if x_type == "Numerical":
            num = x_feature
            cat = y_feature
        else:
            num = y_feature
            cat = x_feature

        means = (
            df.groupby(cat)[num]
            .mean()
            .sort_values(ascending=False)
        )

        highest = means.index[0]
        lowest = means.index[-1]

        insights.append(
            f"{highest} has the highest average {num.replace('_', ' ')}."
        )

        insights.append(
            f"{lowest} has the lowest average {num.replace('_', ' ')}."
        )

        fraud_rates = (
            df.groupby(cat)["is_fraud"]
            .mean()
            .mul(100)
            .sort_values(ascending=False)
        )

        insights.append(
            f"The highest fraud rate is observed for {fraud_rates.index[0]} ({fraud_rates.iloc[0]:.2f}%)."
        )

        insights.append(
            f"The lowest fraud rate is observed for {fraud_rates.index[-1]} ({fraud_rates.iloc[-1]:.2f}%)."
        )


    else:
        pair = (
            df.groupby([x_feature, y_feature])
            .agg(
                Transactions=("is_fraud", "size"),
                Frauds=("is_fraud", "sum"),
            )
            .reset_index()
        )

        pair["Fraud Rate"] = (
            pair["Frauds"] /
            pair["Transactions"] * 100
        )

        pair = pair.sort_values(
            "Fraud Rate",
            ascending=False,
        )

        top = pair.iloc[0]

        insights.append(
            f"The combination '{top[x_feature]}' × '{top[y_feature]}' has the highest fraud rate ({top['Fraud Rate']:.2f}%)."
        )

        insights.append(
            f"This combination contains {int(top['Transactions']):,} transactions."
        )

        insights.append(
            f"There are {df[x_feature].nunique()} unique values in {x_feature.replace('_', ' ')}."
        )

        insights.append(
            f"There are {df[y_feature].nunique()} unique values in {y_feature.replace('_', ' ')}."
        )


    items = ""

    for insight in insights:

        items += (
            f"<li>{check_icon}"
            f"<span>{insight}</span></li>"
        )

    st.markdown(
        f'<div class="insight-card"> <div class="insight-heading"> {panel_icon} </div> <ul class="insight-list"> {items} </ul> </div>',
        unsafe_allow_html=True,
    )