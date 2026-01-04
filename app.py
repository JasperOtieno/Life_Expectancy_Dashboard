import streamlit as st

from config import DATA_PATH, PAGE_CONFIG
from data_loader import load_data, clean_data, validate_data
from sidebar import sidebar_filters, apply_filters, NUMERIC_VARIABLES
from kpis import compute_kpis, render_kpis
from relationships import variable_relationship
from trends import trend_over_time


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

    st.subheader("Relationship Analysis")

    x_var = NUMERIC_VARIABLES[filters["x_variable"]]
    y_var = NUMERIC_VARIABLES[filters["y_variable"]]

    st.plotly_chart(
        variable_relationship(filtered_df, x_var, y_var),
        use_container_width=True
    )

    st.subheader("Trend Analysis")

    trend_var = NUMERIC_VARIABLES[filters["trend_variable"]]

    st.plotly_chart(
        trend_over_time(filtered_df, trend_var),
        use_container_width=True
    )


if __name__ == "__main__":
    main()
