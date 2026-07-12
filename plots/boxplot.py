import plotly.express as px

from plots.theme import PRIMARY, apply_theme


def create(df, column=None, x=None, y=None):
    """
    Create a box plot.
    """


    # Univariate
    if column is not None:
        fig = px.box(
            df,
            y=column,
            color_discrete_sequence=[PRIMARY],
            points="outliers",
        )

        fig.update_traces(
            hovertemplate="<b>%{y}</b><extra></extra>",
            hoverlabel=dict(
                bgcolor="white",
                font=dict(color="#000000"),
            ),
        )

        fig.update_layout(
            title=f"Box Plot of {column.replace('_', ' ').title()}",
        )


    # Bivariate
    else:
        fig = px.box(
            df,
            x=x,
            y=y,
            color=x,
            points="outliers",
        )

        fig.update_traces(
            hovertemplate=(
                f"<b>{x.replace('_', ' ').title()}</b>: %{{x}}"
                f"<br><b>{y.replace('_', ' ').title()}</b>: %{{y}}"
                "<extra></extra>"
            ),
            hoverlabel=dict(
                bgcolor="white",
                font=dict(color="#000000"),
            ),
        )

        fig.update_layout(
            title=f"{y.replace('_', ' ').title()} by {x.replace('_', ' ').title()}",
            showlegend=False,
        )


    return apply_theme(fig)