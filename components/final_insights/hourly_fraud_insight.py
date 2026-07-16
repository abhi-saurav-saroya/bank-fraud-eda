import streamlit as st

from plots.line_chart import create as create_line_chart

from utils.icons import get_svg

pin_icon = get_svg("pin")
check_icon = get_svg("check")


def render(df):
    """
    Render fraud rate by hour of the day.
    """

    st.markdown(
        f'<div class="section"> <h2 class="section-title"> Fraud Risk Throughout the Day </h2> <div class="section-subtitle"> Analyze how fraud rates vary across different hours of the day to identify periods with elevated fraud activity. </div> </div>',
        unsafe_allow_html=True,
    )


    hourly_fraud = (
        df.groupby("hour_of_day")["is_fraud"]
        .mean()
        .mul(100)
        .reset_index()
    )

    hourly_fraud.columns = [
        "Hour of Day",
        "Fraud Rate (%)",
    ]

    fig = create_line_chart(
        df=hourly_fraud,
        x="Hour of Day",
        y="Fraud Rate (%)",
        title="Fraud Rate by Hour of Day",
    )

    fig.update_layout(
        xaxis=dict(
            tickmode="linear",
            dtick=1,
        )
    )

    st.plotly_chart(
        fig,
        width="stretch",
    )


    highest = hourly_fraud.loc[
        hourly_fraud["Fraud Rate (%)"].idxmax()
    ]

    lowest = hourly_fraud.loc[
        hourly_fraud["Fraud Rate (%)"].idxmin()
    ]

    average_rate = hourly_fraud["Fraud Rate (%)"].mean()

    peak_hours = hourly_fraud[
        hourly_fraud["Fraud Rate (%)"] > average_rate
    ]["Hour of Day"].tolist()

    peak_hours_text = ", ".join(str(int(h)) for h in peak_hours)

    insights = []

    insights.append(
        f"The highest fraud rate occurs at <b>{int(highest["Hour of Day"]):02d}:00</b>, where approximately <b>{highest["Fraud Rate (%)"]:.2f}%</b> of transactions are fraudulent."
    )

    insights.append(
        f"The lowest fraud activity is observed at <b>{int(lowest["Hour of Day"]):02d}:00</b>, with a fraud rate of only <b>{lowest["Fraud Rate (%)"]:.2f}%</b>."
    )

    insights.append(
        f"Hours with above-average fraud activity: <b>{peak_hours_text}</b>."
    )

    insights.append(
        f"Several hours consistently record fraud rates above the daily average, indicating that fraud attempts are concentrated during specific periods rather than being uniformly distributed."
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