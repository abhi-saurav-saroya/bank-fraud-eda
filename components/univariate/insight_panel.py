import pandas as pd
import streamlit as st

from utils.icons import get_svg

panel_icon = get_svg("lightbulb")
check_icon = get_svg("check")


def render(df: pd.DataFrame, feature_type: str, feature: str):
    """
    Render automatic insights for the selected feature.
    """

    series = df[feature].dropna()

    st.markdown(
        f'<div class="section"> <h2 class="section-title"> Key Insights </h2> <div class="section-subtitle"> Automatically generated observations for the selected feature. </div> </div>',
        unsafe_allow_html=True,
    )

    insights = []


    if feature_type == "Numerical":

        mean = series.mean()
        median = series.median()
        std = series.std()
        skew = series.skew()

        q1 = series.quantile(0.25)
        q3 = series.quantile(0.75)
        iqr = q3 - q1

        lower = q1 - 1.5 * iqr
        upper = q3 + 1.5 * iqr

        outliers = ((series < lower) | (series > upper)).sum()

        missing = df[feature].isna().sum()

        insights.append(
            f"Mean value is {mean:.2f} while the median is {median:.2f}."
        )

        if mean > median:
            insights.append(
                "Distribution is slightly influenced by larger values."
            )
        elif mean < median:
            insights.append(
                "Distribution is slightly influenced by smaller values."
            )

        if abs(skew) < 0.5:
            insights.append(
                "Distribution is approximately symmetric."
            )
        elif skew > 0:
            insights.append(
                f"Distribution is positively skewed ({skew:.2f})."
            )
        else:
            insights.append(
                f"Distribution is negatively skewed ({skew:.2f})."
            )

        insights.append(
            f"Standard deviation is {std:.2f}."
        )

        insights.append(
            f"Detected {outliers:,} potential outlier(s) using the IQR method."
        )

        if missing == 0:
            insights.append(
                "No missing values are present."
            )
        else:
            insights.append(
                f"Dataset contains {missing} missing value(s)."
            )


    elif feature_type in ("Categorical", "Discrete Numerical"):

        counts = series.value_counts()

        mode = counts.idxmax()
        freq = counts.max()

        unique = series.nunique()

        missing = df[feature].isna().sum()

        percentage = freq / len(series) * 100

        insights.append(
            f"The feature contains {unique} unique categories."
        )

        insights.append(
            f"{mode} is the most frequent category "
            f"({freq:,} records, {percentage:.1f}%)."
        )

        insights.append(
            f"Least frequent category appears {counts.min()} time(s)."
        )

        if missing == 0:
            insights.append(
                "No missing values are present."
            )
        else:
            insights.append(
                f"Dataset contains {missing} missing value(s)."
            )


    elif feature_type == "Binary":

        counts = series.value_counts()

        zeros = counts.get(0, 0)
        ones = counts.get(1, 0)

        total = zeros + ones

        positive = ones / total * 100
        negative = zeros / total * 100

        insights.append(
            f"Positive class represents {positive:.2f}% of the data."
        )

        insights.append(
            f"Negative class represents {negative:.2f}% of the data."
        )

        if positive < 10:
            insights.append(
                "The target distribution is highly imbalanced."
            )
        elif positive < 30:
            insights.append(
                "The positive class is noticeably smaller than the negative class."
            )
        else:
            insights.append(
                "The two classes are relatively balanced."
            )

        insights.append(
            f"Total observations: {total:,}."
        )


    items = ""

    for insight in insights:

        items += f'<li> {check_icon} <span>{insight}</span> </li>'

    st.markdown(
        f'<div class="insight-card"> <div class="insight-heading"> {panel_icon} </div> <ul class="insight-list"> {items} </ul> </div>',
        unsafe_allow_html=True,
    )