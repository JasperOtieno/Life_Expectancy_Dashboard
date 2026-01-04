# Global Life Expectancy and Socioeconomic Indicators Dashboard

## Project Overview

This project explores the relationship between life expectancy and key socioeconomic and health-related indicators across countries and over time. Using publicly available World Bank data, the project combines data analysis, visualization, and interactive dashboard development to support data-driven insights at a global level.

The final output is an interactive Streamlit dashboard that allows users to explore trends, compare countries and regions, and understand how factors such as health expenditure, education spending, unemployment, sanitation, and disease burden relate to life expectancy outcomes.

## Objectives

The main objectives of this project are to:

Analyze global life expectancy trends across countries, regions, and income groups.

Examine associations between life expectancy and socioeconomic indicators such as education, health expenditure, unemployment, and corruption.

Provide an intuitive and interactive dashboard for exploratory data analysis.

Demonstrate best practices in reproducible analytics, modular coding, and deployment-ready applications.

## Dataset Description

The dataset used in this project is sourced from the World Bank and compiled via Kaggle.

**Dataset:** Life Expectancy and Socio-Economic Indicators
**Source:** World Bank
**Access:** https://www.kaggle.com/datasets/mjshri23/life-expectancy-and-socio-economic-world-bank

**Key Variables**

Country Name

Country Code

Region

Income Group

Year

Life Expectancy (World Bank)

Prevalence of Undernourishment

CO₂ Emissions

Health Expenditure (%)

Education Expenditure (%)

Unemployment Rate

Corruption Index

Access to Sanitation

Injury-related Mortality

Communicable Diseases

Non-Communicable Diseases

The dataset spans multiple years, enabling longitudinal analysis and trend visualization.

## Methodology

Load and validate structured CSV data

Clean and filter data by year, region, and income group

Perform exploratory data analysis

Develop interactive visualizations using Plotly

Build and deploy a Streamlit dashboard using GitHub integration

Modular Python code using Streamlit.

## Tools and Technologies

Python

Pandas for data manipulation

Plotly for interactive visualizations

Streamlit for dashboard development and deployment

Git and GitHub for version control

PyCharm for development

R Markdown for documentation and reproducibility

## Key Findings

Based on exploratory analysis of the World Bank life expectancy and socioeconomic dataset, several consistent patterns emerge across countries and regions.

First, life expectancy shows a strong positive association with income group. High-income countries consistently exhibit higher life expectancy compared to low- and lower-middle-income countries. The gap persists over time, although gradual improvements are observed in most regions.

Second, health expenditure and access to sanitation are positively associated with life expectancy. Countries with higher health spending as a percentage of GDP and broader access to sanitation services tend to record better life expectancy outcomes. This relationship is particularly pronounced in middle-income countries, where incremental investments appear to yield substantial gains.

Third, disease burden patterns differ by development level. Communicable diseases and injury-related mortality are more prevalent in low-income regions, while non-communicable diseases dominate in high-income settings. This reflects an epidemiological transition as countries develop.

Fourth, education expenditure shows a moderate but consistent relationship with life expectancy, suggesting indirect effects through improved health literacy, employment, and long-term socioeconomic stability.

Finally, regional disparities remain significant, even within the same income group. This highlights the influence of contextual factors such as governance, infrastructure, and health system efficiency beyond economic classification alone.

These findings are exploratory in nature and do not imply causation. However, they provide a useful foundation for policy-oriented discussion and further statistical modeling.