import pandas as pd
import os

INPUT_FILE = "data/curated/retail_master_curated.csv"

print("=" * 60)
print("STAR SCHEMA GENERATION")
print("=" * 60)

# Create output folder
os.makedirs(
    "data/curated/star_schema",
    exist_ok=True
)

# Load curated dataset
df = pd.read_csv(INPUT_FILE)

# --------------------------------------------------
# DimProduct
# --------------------------------------------------

dim_product = df[
    [
        "product_id",
        "product_name",
        "category",
        "price"
    ]
].drop_duplicates()

# --------------------------------------------------
# DimCustomer
# --------------------------------------------------

dim_customer = df[
    [
        "customer_id",
        "customer_name",
        "email_masked",
        "phone_masked"
    ]
].drop_duplicates()

# --------------------------------------------------
# DimDate
# --------------------------------------------------

dim_date = df[
    [
        "transaction_date",
        "Year",
        "Month",
        "Quarter"
    ]
].drop_duplicates()

# --------------------------------------------------
# DimLocation
# --------------------------------------------------

dim_location = df[
    [
        "city",
        "purchase_location"
    ]
].drop_duplicates()

# --------------------------------------------------
# FactSales
# --------------------------------------------------

fact_sales = df[
    [
        "transaction_id",
        "customer_id",
        "product_id",
        "transaction_date",
        "quantity",
        "price",
        "Revenue",
        "Discount_Amount",
        "Net_Revenue",
        "payment_method",
        "payment_status"
    ]
]

# --------------------------------------------------
# Save Tables
# --------------------------------------------------

dim_product.to_csv(
    "data/curated/star_schema/DimProduct.csv",
    index=False
)

dim_customer.to_csv(
    "data/curated/star_schema/DimCustomer.csv",
    index=False
)

dim_date.to_csv(
    "data/curated/star_schema/DimDate.csv",
    index=False
)

dim_location.to_csv(
    "data/curated/star_schema/DimLocation.csv",
    index=False
)

fact_sales.to_csv(
    "data/curated/star_schema/FactSales.csv",
    index=False
)

print("\nStar Schema Created Successfully!")

print("\nTable Counts:")

print(f"DimProduct : {len(dim_product)}")
print(f"DimCustomer : {len(dim_customer)}")
print(f"DimDate : {len(dim_date)}")
print(f"DimLocation : {len(dim_location)}")
print(f"FactSales : {len(fact_sales)}")