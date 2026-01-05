
# Sidebar filter creation and application.

import streamlit as st
import pandas as pd


NUMERIC_VARIABLES = {
    "Life Expectancy": "life_expectancy",
    "CO2 Emissions": "co2_emissions",
    "Health Expenditure (%)": "health_exp_pct",
    "Education Expenditure (%)": "education_exp_pct",
    "Unemployment (%)": "unemployment",
    "Sanitation Access (%)": "sanitation_access",
    "Undernourishment": "undernourishment",
    "Communicable Diseases": "communicable",
    "Non-Communicable Diseases": "non_communicable",
    "Injuries": "injuries",
    "Corruption Index": "corruption_index"
}


def sidebar_filters(df: pd.DataFrame) -> dict:
    #st.sidebar.header("Filters")
    st.sidebar.subheader("Population Filters")

    # Set default values if they exist in the dataframe
    default_region = "Sub-Saharan Africa" if "Sub-Saharan Africa" in df["region"].unique() else None
    default_country = "Kenya" if "Kenya" in df["country"].unique() else None
    default_income = "Lower middle income" if "Lower middle income" in df["income_group"].unique() else None

    filters = {
        "regions": st.sidebar.multiselect(
            "Region",
            sorted(df["region"].unique()),
            default=[default_region] if default_region else sorted(df["region"].unique())
        ),
        "countries": st.sidebar.multiselect(
            "Country",
            sorted(df["country"].unique()),
            default=[default_country] if default_country else sorted(df["country"].unique())
        ),
        "income_groups": st.sidebar.multiselect(
            "Income Group",
            sorted(df["income_group"].unique()),
            default=[default_income] if default_income else sorted(df["income_group"].unique())
        ),
        "year_range": st.sidebar.slider(
            "Year Range",
            int(df["year"].min()),
            int(df["year"].max()),
            (int(df["year"].min()), int(df["year"].max()))
        )
    }

    st.sidebar.subheader("Analysis Controls")

    filters["trend_variable"] = st.sidebar.selectbox(
        "Trend Variable",
        list(NUMERIC_VARIABLES.keys()),
        index=0
    )

    filters["x_variable"] = st.sidebar.selectbox(
        "X-axis Variable",
        list(NUMERIC_VARIABLES.keys()),
        index=1
    )

    filters["y_variable"] = st.sidebar.selectbox(
        "Y-axis Variable",
        list(NUMERIC_VARIABLES.keys()),
        index=0
    )

    return filters


def apply_filters(df: pd.DataFrame, filters: dict) -> pd.DataFrame:
    start_year, end_year = filters["year_range"]

    return df[
        (df["region"].isin(filters["regions"])) &
        (df["country"].isin(filters["countries"])) &
        (df["income_group"].isin(filters["income_groups"])) &
        (df["year"].between(start_year, end_year))
    ]
