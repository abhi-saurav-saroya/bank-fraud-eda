import streamlit as st


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
        st.markdown(
            f'<div class="metric-card"> <div class="metric-icon"> 💳 </div> <div class="metric-value"> {total_transactions:,} </div> <div class="metric-title"> Total Transactions </div> </div>',
            unsafe_allow_html=True,
        )

    with c2:
        st.markdown(
            f'<div class="metric-card"> <div class="metric-icon"> 🚨 </div> <div class="metric-value"> {fraud_rate:.2f}% </div> <div class="metric-title"> Fraud Rate </div> </div>',
            unsafe_allow_html=True,
        )

    with c3:
        st.markdown(
            f'<div class="metric-card"> <div class="metric-icon"> 🌍 </div> <div class="metric-value"> {international_transactions:,} </div> <div class="metric-title"> International Transactions </div> </div>',
            unsafe_allow_html=True,
        )

    with c4:
        st.markdown(
            f'<div class="metric-card"> <div class="metric-icon"> 📂 </div> <div class="metric-value"> {total_features} </div> <div class="metric-title"> Features Count </div> </div>',
            unsafe_allow_html=True,
        )