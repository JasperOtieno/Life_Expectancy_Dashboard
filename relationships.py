
# Cross-sectional relationship plots.

import plotly.express as px
import pandas as pd


def life_expectancy_vs_co2(df: pd.DataFrame):
    return px.scatter(
        df,
        x="co2_emissions",
        y="life_expectancy",
        color="income_group",
        hover_name="country",
        title="Life Expectancy vs CO₂ Emissions"
    )


def health_expenditure_vs_life(df: pd.DataFrame):
    return px.scatter(
        df,
        x="health_exp_pct",
        y="life_expectancy",
        color="region",
        hover_name="country",
        title="Health Expenditure vs Life Expectancy"
    )
