import plotly.graph_objects as go

from plots.theme import PRIMARY, PRIMARY_LIGHT, apply_theme


def create(df, features, target="is_fraud"):
    """
    Radar chart comparing Fraud vs Legitimate.
    """

    legit = (
        df[df[target] == 0][features]
        .mean()
    )

    fraud = (
        df[df[target] == 1][features]
        .mean()
    )

    fig = go.Figure()

    fig.add_trace(
        go.Scatterpolar(
            r=legit.values,
            theta=features,
            fill="toself",
            name="Legitimate",
            line=dict(color=PRIMARY),
        )
    )

    fig.add_trace(
        go.Scatterpolar(
            r=fraud.values,
            theta=features,
            fill="toself",
            name="Fraud",
            line=dict(color=PRIMARY_LIGHT),
        )
    )

    fig.update_layout(
        polar=dict(radialaxis=dict(visible=True)),
        title="Fraud Profile Comparison",
    )

    return apply_theme(fig)