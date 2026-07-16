import plotly.express as px

from plots.theme import PRIMARY, apply_theme


def create(df, x, y, title=None, markers=True, color=None):
    """
    Create a reusable line chart.
    """

    fig = px.line(
        df,
        x=x,
        y=y,
        color=color,
        markers=markers,
    )

    fig.update_traces(
        line=dict(
            width=3,
            color=PRIMARY,
        ),
        marker=dict(
            size=9,
            color=PRIMARY,
            line=dict(
                width=2,
                color="white",
            ),
        ),
        hovertemplate=(
            "<b>%{x}</b>"
            "<br>%{y:.2f}"
            "<extra></extra>"
        ),
        hoverlabel=dict(
            bgcolor="white",
            font=dict(
                color="#000000",
            ),
        ),
    )

    fig.update_layout(
        title=title,
        xaxis_title=x.replace("_", " ").title(),
        yaxis_title=y.replace("_", " ").title(),
    )

    return apply_theme(fig)