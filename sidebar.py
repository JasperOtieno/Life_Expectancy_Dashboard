
# Sidebar filter creation and application.

import streamlit as st
import pandas as pd

# Render sidebar widgets and return selected filters.
def sidebar_filters(df: pd.DataFrame) -> dict:

    st.sidebar.header("Filters")

    return {
        "regions": st.sidebar.multiselect(
            "Region",
            sorted(df["region"].unique()),
            default=sorted(df["region"].unique())
        ),
        "countries": st.sidebar.multiselect(
            "Country",
            sorted(df["country"].unique()),
            default=sorted(df["country"].unique())
        ),
        "income_groups": st.sidebar.multiselect(
            "Income Group",
            sorted(df["income_group"].unique()),
            default=sorted(df["income_group"].unique())
        ),
        "year": st.sidebar.slider(
            "Year",
            int(df["year"].min()),
            int(df["year"].max()),
            int(df["year"].max())
        )
    }

# Apply sidebar filters to the dataset.
def apply_filters(df: pd.DataFrame, filters: dict) -> pd.DataFrame:

    return df[
        (df["region"].isin(filters["regions"])) &
        (df["country"].isin(filters["countries"])) &
        (df["income_group"].isin(filters["income_groups"])) &
        (df["year"] == filters["year"])
    ]
