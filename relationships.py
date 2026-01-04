
# Scatter plot for relationship between two indicators.

import plotly.express as px
import pandas as pd


def variable_relationship(
    df: pd.DataFrame,
    x_col: str,
    y_col: str
):

    return px.scatter(
        df,
        x=x_col,
        y=y_col,
        color="income_group",
        hover_name="country",
        title=f"{y_col.replace('_', ' ').title()} vs {x_col.replace('_', ' ').title()}",
        trendline="ols"
    )
