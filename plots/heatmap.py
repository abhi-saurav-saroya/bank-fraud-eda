import pandas as pd
import plotly.express as px

from plots.theme import apply_theme


def create(df, x, y):
    """
    Create heatmap for two categorical variables.
    """

    table = pd.crosstab(
        df[y],
        df[x],
    )

    fig = px.imshow(
        table,
        text_auto=True,
        aspect="auto",
        color_continuous_scale="Blues",
    )

    fig.update_traces(
        hovertemplate=(
            "<b>X:</b> %{x}"
            "<br><b>Y:</b> %{y}"
            "<br><b>Count:</b> %{z}"
            "<extra></extra>"
        ),
        hoverlabel=dict(
            bgcolor="white",
            font=dict(color="#000000"),
        ),
    )

    fig.update_layout(
        title=f"{y.replace('_',' ').title()} vs {x.replace('_',' ').title()}",
    )

    return apply_theme(fig)