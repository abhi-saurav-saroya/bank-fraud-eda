import plotly.express as px

from plots.theme import apply_theme


def create(df, features, target="is_fraud"):
    """
    Scatter matrix.
    """

    fig = px.scatter_matrix(
        df,
        dimensions=features,
        color=target,
    )

    fig.update_traces(
        diagonal_visible=False,
    )

    fig.update_layout(
        title="Scatter Matrix",
    )

    return apply_theme(fig)