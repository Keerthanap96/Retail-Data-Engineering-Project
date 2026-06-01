import pandas as pd
import os

INPUT_FILE = "data/curated/retail_master_curated.csv"

print("=" * 60)
print("KPI GENERATION")
print("=" * 60)

# Create KPI folder
os.makedirs(
    "data/curated/kpis",
    exist_ok=True
)

# Load curated dataset
df = pd.read_csv(INPUT_FILE)

# ==================================================
# KPI 1 - Executive Summary
# ==================================================

executive_summary = pd.DataFrame({
    "Metric": [
        "Total Revenue",
        "Total Net Revenue",
        "Total Orders",
        "Total Customers",
        "Average Order Value"
    ],
    "Value": [
        df["Revenue"].sum(),
        df["Net_Revenue"].sum(),
        df["transaction_id"].nunique(),
        df["customer_id"].nunique(),
        df["Revenue"].mean()
    ]
})

# ==================================================
# KPI 2 - Category Analysis
# ==================================================

category_analysis = (
    df.groupby("category")
    .agg(
        Revenue=("Revenue", "sum"),
        Net_Revenue=("Net_Revenue", "sum"),
        Orders=("transaction_id", "nunique")
    )
    .reset_index()
)

# ==================================================
# KPI 3 - City Analysis
# ==================================================

city_analysis = (
    df.groupby("city")
    .agg(
        Revenue=("Revenue", "sum"),
        Net_Revenue=("Net_Revenue", "sum"),
        Orders=("transaction_id", "nunique")
    )
    .reset_index()
)

# ==================================================
# KPI 4 - Product Analysis
# ==================================================

product_analysis = (
    df.groupby("product_name")
    .agg(
        Revenue=("Revenue", "sum"),
        Net_Revenue=("Net_Revenue", "sum"),
        Quantity_Sold=("quantity", "sum"),
        Orders=("transaction_id", "nunique")
    )
    .reset_index()
)

# ==================================================
# KPI 5 - Customer Analysis
# ==================================================

customer_analysis = (
    df.groupby(
        ["customer_id", "customer_name"]
    )
    .agg(
        Revenue=("Revenue", "sum"),
        Orders=("transaction_id", "nunique")
    )
    .reset_index()
)

# ==================================================
# KPI 6 - Payment Analysis
# ==================================================

payment_analysis = (
    df.groupby(
        ["payment_method", "payment_status"]
    )
    .agg(
        Revenue=("Revenue", "sum"),
        Orders=("transaction_id", "nunique")
    )
    .reset_index()
)

# ==================================================
# KPI 7 - Time Analysis
# ==================================================

time_analysis = (
    df.groupby(
        ["Year", "Quarter", "Month"]
    )
    .agg(
        Revenue=("Revenue", "sum"),
        Net_Revenue=("Net_Revenue", "sum"),
        Orders=("transaction_id", "nunique")
    )
    .reset_index()
)

# ==================================================
# KPI 8 - Data Quality
# ==================================================

data_quality = pd.read_csv(
    "outputs/cleaning_summary.csv"
)

# ==================================================
# Save KPI Files
# ==================================================

executive_summary.to_csv(
    "data/curated/kpis/kpi_executive_summary.csv",
    index=False
)

category_analysis.to_csv(
    "data/curated/kpis/kpi_category_analysis.csv",
    index=False
)

city_analysis.to_csv(
    "data/curated/kpis/kpi_city_analysis.csv",
    index=False
)

product_analysis.to_csv(
    "data/curated/kpis/kpi_product_analysis.csv",
    index=False
)

customer_analysis.to_csv(
    "data/curated/kpis/kpi_customer_analysis.csv",
    index=False
)

payment_analysis.to_csv(
    "data/curated/kpis/kpi_payment_analysis.csv",
    index=False
)

time_analysis.to_csv(
    "data/curated/kpis/kpi_time_analysis.csv",
    index=False
)

data_quality.to_csv(
    "data/curated/kpis/kpi_data_quality.csv",
    index=False
)

print("\nKPI Files Generated Successfully!")

print("\nGenerated KPI Files:")

print("kpi_executive_summary.csv")
print("kpi_category_analysis.csv")
print("kpi_city_analysis.csv")
print("kpi_product_analysis.csv")
print("kpi_customer_analysis.csv")
print("kpi_payment_analysis.csv")
print("kpi_time_analysis.csv")
print("kpi_data_quality.csv")