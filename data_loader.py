"""
Data loading, cleaning, and validation utilities.
"""

import pandas as pd
import streamlit as st

# Load and preprocess the life expectancy dataset.

@st.cache_data
def load_data(path: str) -> pd.DataFrame:

    df = pd.read_csv(path)

    df = df.rename(columns={
        "Country Name": "country",
        "Country Code": "country_code",
        "Region": "region",
        "IncomeGroup": "income_group",
        "Year": "year",
        "Life Expectancy World Bank": "life_expectancy",
        "Prevelance of Undernourishment": "undernourishment",
        "CO2": "co2_emissions",
        "Health Expenditure %": "health_exp_pct",
        "Education Expenditure %": "education_exp_pct",
        "Unemployment": "unemployment",
        "Corruption": "corruption_index",
        "Sanitation": "sanitation_access",
        "Injuries": "injuries",
        "Communicable": "communicable",
        "NonCommunicable": "non_communicable"
    })

    numeric_cols = [
        "year", "life_expectancy", "undernourishment", "co2_emissions",
        "health_exp_pct", "education_exp_pct", "unemployment",
        "corruption_index", "sanitation_access",
        "injuries", "communicable", "non_communicable"
    ]

    df[numeric_cols] = df[numeric_cols].apply(pd.to_numeric, errors="coerce")

    return df

# Remove rows with missing key identifiers.
def clean_data(df: pd.DataFrame) -> pd.DataFrame:

    return df.dropna(subset=["region", "country", "year", "income_group"])

# Validate presence of required columns.
def validate_data(df: pd.DataFrame) -> None:

    required_cols = ["region", "country", "year", "income_group"]
    missing = [c for c in required_cols if c not in df.columns]

    if missing:
        st.error(f"Missing required columns: {missing}")
        st.stop()
