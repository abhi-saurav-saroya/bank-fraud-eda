import plotly.express as px

from plots.theme import apply_theme


def create(df, columns):
    """
    Create a correlation heatmap.
    """

    corr = df[columns].corr(numeric_only=True)

    fig = px.imshow(
        corr,
        text_auto=".2f",
        color_continuous_scale="RdBu_r",
        aspect="auto",
        zmin=-1,
        zmax=1,
    )

    fig.update_layout(
        title="Correlation Heatmap",
    )

    return apply_theme(fig)