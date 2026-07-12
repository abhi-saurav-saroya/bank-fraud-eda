import pandas as pd
import plotly.express as px

from plots.theme import COLORS, apply_theme


def create(df, x, y):
    """
    Create grouped bar chart for two categorical variables.
    """

    counts = (
        df.groupby([x, y])
        .size()
        .reset_index(name="Count")
    )

    counts[x] = counts[x].astype(str)
    counts[y] = counts[y].astype(str)

    fig = px.bar(
        counts,
        x=x,
        y="Count",
        color=y,
        barmode="group",
        color_discrete_sequence=COLORS,
    )

    fig.update_traces(
        hovertemplate=(
            "<b>%{x}</b>"
            "<br>Count: %{y}"
            "<extra></extra>"
        ),
        hoverlabel=dict(
            bgcolor="white",
            font=dict(color="#000000"),
        ),
    )

    fig.update_layout(
        title=f"{x.replace('_',' ').title()} vs {y.replace('_',' ').title()}",
    )

    return apply_theme(fig)