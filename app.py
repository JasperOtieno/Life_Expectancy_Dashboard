import streamlit as st

from config import DATA_PATH, PAGE_CONFIG
from data_loader import load_data, clean_data, validate_data
from sidebar import sidebar_filters, apply_filters
from kpis import compute_kpis, render_kpis
from relationships import life_expectancy_vs_co2, health_expenditure_vs_life
from trends import country_life_expectancy_trend


def main() -> None:
    st.set_page_config(**PAGE_CONFIG)

    st.title("Global Life Expectancy and Socio-Economic Indicators")

    df = load_data(DATA_PATH)
    df = clean_data(df)
    validate_data(df)

    filters = sidebar_filters(df)
    filtered_df = apply_filters(df, filters)

    if filtered_df.empty:
        st.warning("No data available for selected filters.")
        return

    st.subheader("Key Performance Indicators")
    render_kpis(compute_kpis(filtered_df))

    st.subheader("Cross-Sectional Relationships")
    col1, col2 = st.columns(2)

    with col1:
        st.plotly_chart(life_expectancy_vs_co2(filtered_df), use_container_width=True)

    with col2:
        st.plotly_chart(health_expenditure_vs_life(filtered_df), use_container_width=True)

    st.subheader("Country Trend Analysis")
    country = st.selectbox("Select Country", sorted(df["country"].unique()))

    st.plotly_chart(
        country_life_expectancy_trend(df, country),
        use_container_width=True
    )


if __name__ == "__main__":
    main()
