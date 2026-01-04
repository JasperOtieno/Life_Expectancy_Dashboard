
# Time series trend analysis.


import plotly.express as px
import pandas as pd

# Plot time trend for selected variable across countries.
def trend_over_time(
    df: pd.DataFrame,
    value_column: str
):

    aggregated = (
        df.groupby(["year", "country"], as_index=False)[value_column]
        .mean()
    )

    return px.line(
        aggregated,
        x="year",
        y=value_column,
        color="country",
        title=f"Trend Over Time: {value_column.replace('_', ' ').title()}",
        markers=False
    )