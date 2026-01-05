"""
KPI computation and rendering.
"""

import streamlit as st
import pandas as pd

# Compute dashboard KPIs.
def compute_kpis(df: pd.DataFrame) -> dict:

    return {
        "Life Expectancy": round(df["life_expectancy"].mean(), 2),
        "Unemployment (%)": round(df["unemployment"].mean(), 2),
        "Sanitation Access (%)": round(df["sanitation_access"].mean(), 2),
        "Health Expenditure (%)": round(df["health_exp_pct"].mean(), 2),
        "Education Expenditure (%)": round(df["education_exp_pct"].mean(), 2),
        "Undernourishment": round(df["undernourishment"].mean(), 2),
        "CO2 Emissions": round(df["co2_emissions"].mean(), 2),
        "Corruption Index": round(df["corruption_index"].mean(), 2),
        "Injury related deaths": round(df["injuries"].mean(), 2),
        "Communicable Diseases": round(df["communicable"].mean(), 2),
        "Non Communicable Diseases": round(df["non_communicable"].mean(), 2)
    }

# Render KPI cards in multiple rows to avoid compression.
def render_kpis(kpis: dict) -> None:

    kpi_items = list(kpis.items())

    rows = [
        kpi_items[:4],
        kpi_items[4:8],
        kpi_items[8:]
    ]

    for row in rows:
        cols = st.columns(len(row))
        for col, (label, value) in zip(cols, row):
            col.metric(label, value)
