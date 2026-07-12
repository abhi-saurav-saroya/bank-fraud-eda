import plotly.express as px

from plots.theme import apply_theme


def create(df, x, y, color=None):
    """
    Create a scatter plot.
    """

    fig = px.scatter(
        df,
        x=x,
        y=y,
        color=color,
        opacity=0.75,
    )

    fig.update_traces(
        marker=dict(
            size=8,
            line=dict(width=0),
        ),
        hoverlabel=dict(
            bgcolor="white",
            font=dict(color="#000000"),
        ),
        hovertemplate=(
            f"<b>{x.replace('_',' ').title()}</b>: %{{x}}"
            f"<br><b>{y.replace('_',' ').title()}</b>: %{{y}}"
            "<extra></extra>"
        ),
    )

    fig.update_layout(
        title=f"{y.replace('_',' ').title()} vs {x.replace('_',' ').title()}",
    )

    return apply_theme(fig)