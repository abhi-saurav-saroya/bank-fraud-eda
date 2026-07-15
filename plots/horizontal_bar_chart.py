import plotly.express as px

from plots.theme import COLORS, apply_theme


def create(data, x, y, title):
    """
    Create a horizontal bar chart.
    """

    fig = px.bar(
        data,
        x=x,
        y=y,
        orientation="h",
        color=y,
        color_continuous_scale=COLORS,
    )

    fig.update_traces(
        hovertemplate=(
            "<b>%{y}</b>"
            "<br>Value: %{x:.3f}"
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
        coloraxis_showscale=False,
    )

    return apply_theme(fig)