import streamlit as st

from utils.icons import get_svg

from components.metric_card import render as render_metric_card

credit_card_icon = get_svg("credit-card")
siren_icon = get_svg("siren")
globe_icon = get_svg("earth")
folder_icon = get_svg("folder-closed")

def render(df):
    """
    Render dashboard KPI cards.
    """

    total_transactions = len(df)
    fraud_rate = df["is_fraud"].mean() * 100
    total_features = df.shape[1]

    international_transactions = (
        df["is_international"].sum()
    )

    c1, c2, c3, c4 = st.columns(4)

    with c1:
        render_metric_card(
            icon=credit_card_icon,
            value=f"{total_transactions:,}",
            label="Total Transactions"
        )

    with c2:
        render_metric_card(
            icon=siren_icon,
            value=f"{fraud_rate:.2f}%",
            label="Fraud Rate"
        )

    with c3:
        render_metric_card(
            icon=globe_icon,
            value=f"{international_transactions:,}",
            label="International Records"
        )

    with c4:
        render_metric_card(
            icon=folder_icon,
            value=total_features,
            label="Features Count"
        )