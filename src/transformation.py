import pandas as pd

INPUT_FILE = "data/processed/retail_master_cleaned.csv"

print("=" * 60)
print("TRANSFORMATION PIPELINE")
print("=" * 60)

# Load cleaned dataset
df = pd.read_csv(INPUT_FILE)

# --------------------------------------------------
# Revenue
# --------------------------------------------------

df["Revenue"] = df["price"] * df["quantity"]

# --------------------------------------------------
# Discount Amount
# --------------------------------------------------

df["Discount_Amount"] = (
    df["Revenue"] * df["discount"]
)

# --------------------------------------------------
# Net Revenue
# --------------------------------------------------

df["Net_Revenue"] = (
    df["Revenue"] - df["Discount_Amount"]
)

# --------------------------------------------------
# Date Features
# --------------------------------------------------

df["transaction_date"] = pd.to_datetime(
    df["transaction_date"]
)

df["Year"] = df["transaction_date"].dt.year

df["Month"] = df["transaction_date"].dt.month_name()

df["Quarter"] = (
    "Q"
    + df["transaction_date"].dt.quarter.astype(str)
)

# --------------------------------------------------
# Save Curated Dataset
# --------------------------------------------------

OUTPUT_FILE = "data/curated/retail_master_curated.csv"

df.to_csv(
    OUTPUT_FILE,
    index=False
)

print("\nTransformation Completed Successfully!")

print(f"Rows: {len(df)}")
print(f"Columns: {df.shape[1]}")

print("\nNew Columns Added:")
print([
    "Revenue",
    "Discount_Amount",
    "Net_Revenue",
    "Year",
    "Month",
    "Quarter"
])