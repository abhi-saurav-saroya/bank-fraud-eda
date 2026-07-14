import plotly.express as px

from plots.theme import apply_theme


def create(df, features, target="is_fraud"):
    """
    Parallel Coordinates Plot.
    """

    fig = px.parallel_coordinates(
        df,
        dimensions=features,
        color=target,
        color_continuous_scale=[
            (0.0, "#2563EB"),
            (1.0, "#EF4444"),
        ],
    )

    fig.update_layout(
        title="Parallel Coordinates",
    )

    return apply_theme(fig)