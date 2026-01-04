"""
KPI computation and rendering.
"""

import streamlit as st
import pandas as pd

# Compute dashboard KPIs.
def compute_kpis(df: pd.DataFrame) -> dict:

    return {
        "Life Expectancy": round(df["life_expectancy"].mean(), 1),
        "Unemployment (%)": round(df["unemployment"].mean(), 1),
        "Sanitation (%)": round(df["sanitation_access"].mean(), 1),
        "Health Expenditure (%)": round(df["health_exp_pct"].mean(), 1),
        "Education Expenditure (%)": round(df["education_exp_pct"].mean(), 1),
        "Undernourishment": round(df["undernourishment"].mean(), 1),
        "CO2 Emissions": round(df["co2_emissions"].mean(), 1),
        "Corruption Index": round(df["corruption_index"].mean(), 1)
    }

# Render KPI cards in multiple rows to avoid compression.
def render_kpis(kpis: dict) -> None:

    kpi_items = list(kpis.items())

    rows = [
        kpi_items[:4],
        kpi_items[4:]
    ]

    for row in rows:
        cols = st.columns(len(row))
        for col, (label, value) in zip(cols, row):
            col.metric(label, value)
