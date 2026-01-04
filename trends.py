
# Time series trend analysis.


import plotly.express as px
import pandas as pd


def country_life_expectancy_trend(df: pd.DataFrame, country: str):
    country_df = df[df["country"] == country]

    return px.line(
        country_df,
        x="year",
        y="life_expectancy",
        title=f"Life Expectancy Trend: {country}"
    )
