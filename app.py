import streamlit as st
import pandas as pd
import plotly.express as px



# Configuration

DATA_PATH = "life_expectancy_world_bank.csv"

# Set page title and layout
def configure_app() -> None:
    st.set_page_config(
        page_title="Life Expectancy & Socio-Economic Dashboard",
        layout="wide"
    )

# Data Layer

@st.cache_data
def load_data(path: str) -> pd.DataFrame:

    df = pd.read_csv(path)

    # rename variables

    df = df.rename(columns={
        "Country Name": "country",
        "Country Code": "country_code",
        "Region": "region",
        "IncomeGroup": "income_group",
        "Year": "year",
        "Life Expectancy World Bank": "life_expectancy",
        "Prevelance of Undernourishment": "undernourishment",
        "CO2": "co2",
        "Health Expenditure %": "health_exp_pct",
        "Education Expenditure %": "education_exp_pct",
        "Unemployment": "unemployment",
        "Corruption": "corruption",
        "Sanitation": "sanitation",
        "Injuries": "injuries",
        "Communicable": "communicable",
        "NonCommunicable": "non_communicable"
    })

    numeric_cols = [
        "year", "life_expectancy", "undernourishment", "co2",
        "health_exp_pct", "education_exp_pct", "unemployment",
        "corruption", "sanitation", "injuries",
        "communicable", "non_communicable"
    ]

    df[numeric_cols] = df[numeric_cols].apply(
        pd.to_numeric, errors="coerce"
    )

    return df

# drop na
def clean_data(df: pd.DataFrame) -> pd.DataFrame:
    df = df.dropna(subset=["country", "year", "life_expectancy"])
    return df

# validate required columns not missing

def validate_data(df: pd.DataFrame) -> None:
    required_cols = ["country", "year", "life_expectancy"]
    missing = [c for c in required_cols if c not in df.columns]

    if missing:
        st.error(f"Missing required columns: {missing}")
        st.stop()

# Render sidebar filters

def sidebar_filters(df: pd.DataFrame) -> dict:
    st.sidebar.header("Filters")

    return {
        "regions": st.sidebar.multiselect(
            "Region",
            options=sorted(df["region"].dropna().unique()),
            default=sorted(df["region"].dropna().unique())
        ),
        "income_groups": st.sidebar.multiselect(
            "Income Group",
            options=sorted(df["income_group"].dropna().unique()),
            default=sorted(df["income_group"].dropna().unique())
        ),
        "year": st.sidebar.slider(
            "Year",
            min_value=int(df["year"].min()),
            max_value=int(df["year"].max()),
            value=int(df["year"].max())
        )
    }

# Apply user-selected filters
def apply_filters(df: pd.DataFrame, filters: dict) -> pd.DataFrame:
    return df[
        (df["region"].isin(filters["regions"])) &
        (df["income_group"].isin(filters["income_groups"])) &
        (df["year"] == filters["year"])
    ]


# Compute dashboard KPIs

def compute_kpis(df: pd.DataFrame) -> dict:
    return {
        "avg_life_exp": round(df["life_expectancy"].mean(), 1),
        "avg_unemployment": round(df["unemployment"].mean(), 1),
        "avg_sanitation": round(df["sanitation"].mean(), 1)
    }

# Render KPI cards
def render_kpis(kpis: dict) -> None:
    col1, col2, col3 = st.columns(3)

    col1.metric("Average Life Expectancy", kpis["avg_life_exp"])
    col2.metric("Average Unemployment (%)", kpis["avg_unemployment"])
    col3.metric("Average Sanitation Coverage (%)", kpis["avg_sanitation"])


# Visualizations
# 1.0 Scatter plot of CO2 vs Life Expectancy

def plot_life_expectancy_vs_co2(df: pd.DataFrame):
    return px.scatter(
        df,
        x="co2",
        y="life_expectancy",
        color="income_group",
        hover_name="country",
        title="Life Expectancy vs CO₂ Emissions"
    )

# Scatter plot of health expenditure vs life expectancy
def plot_health_spend_vs_life(df: pd.DataFrame):
    return px.scatter(
        df,
        x="health_exp_pct",
        y="life_expectancy",
        color="region",
        hover_name="country",
        title="Health Expenditure vs Life Expectancy"
    )

# Time trend for selected country

def plot_country_trend(df: pd.DataFrame, country: str):
    country_df = df[df["country"] == country]

    return px.line(
        country_df,
        x="year",
        y="life_expectancy",
        title=f"Life Expectancy Trend: {country}"
    )


# Main Application

def main() -> None:
    configure_app()
    st.title("Global Life Expectancy and Socio-Economic Indicators")

    df = load_data(DATA_PATH)
    validate_data(df)

    filters = sidebar_filters(df)
    filtered_df = apply_filters(df, filters)

    if filtered_df.empty:
        st.warning("No data available for the selected filters.")
        return

    render_kpis(compute_kpis(filtered_df))

    st.subheader("Cross-Sectional Relationships")
    col1, col2 = st.columns(2)

    with col1:
        st.plotly_chart(
            plot_life_expectancy_vs_co2(filtered_df),
            use_container_width=True
        )

    with col2:
        st.plotly_chart(
            plot_health_spend_vs_life(filtered_df),
            use_container_width=True
        )

    st.subheader("Country Trend Analysis")
    country = st.selectbox(
        "Select Country",
        options=sorted(df["country"].unique())
    )

    st.plotly_chart(
        plot_country_trend(df, country),
        use_container_width=True
    )


if __name__ == "__main__":
    main()
