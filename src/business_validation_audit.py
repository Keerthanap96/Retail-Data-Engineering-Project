import pandas as pd
import re

FILE_PATH = "data/raw/USECASE - Data Engineering.xlsx"

# Load data
products = pd.read_excel(FILE_PATH, sheet_name="product_details")

retail1 = pd.read_excel(FILE_PATH, sheet_name="retail_data1")
retail2 = pd.read_excel(FILE_PATH, sheet_name="retail_data2")

df = pd.concat([retail1, retail2], ignore_index=True)

print("=" * 70)
print("BUSINESS VALIDATION AUDIT")
print("=" * 70)

# --------------------------------------------------
# Product Master Validation
# --------------------------------------------------

orphan_products = df[
    ~df["product_id"].isin(products["product_id"])
]

print(f"\nOrphan Product IDs: {len(orphan_products)}")

# --------------------------------------------------
# Price Consistency Validation
# --------------------------------------------------

price_lookup = dict(
    zip(products["product_id"], products["price"])
)

df["master_price"] = df["product_id"].map(price_lookup)

price_mismatch = df[
    (df["price"].notnull()) &
    (df["master_price"].notnull()) &
    (df["price"] != df["master_price"])
]

print(f"Price Mismatches: {len(price_mismatch)}")

# --------------------------------------------------
# Discount Validation
# --------------------------------------------------

negative_discount = (df["discount"] < 0).sum()

print(f"Negative Discounts: {negative_discount}")

# --------------------------------------------------
# Payment Method Validation
# --------------------------------------------------

print("\nPayment Methods:")
print(sorted(df["payment_method"].astype(str).unique()))

# --------------------------------------------------
# Payment Status Validation
# --------------------------------------------------

print("\nPayment Status Values:")
print(sorted(df["payment_status"].astype(str).unique()))

# --------------------------------------------------
# City Validation
# --------------------------------------------------

print("\nCities:")
print(sorted(df["city"].astype(str).unique()))

# --------------------------------------------------
# Email Validation
# --------------------------------------------------

email_pattern = r"^[^@]+@[^@]+\.[^@]+$"

invalid_emails = df[
    ~df["email"].astype(str).str.match(email_pattern)
]

print(f"\nInvalid Emails: {len(invalid_emails)}")

# --------------------------------------------------
# Phone Validation
# --------------------------------------------------

invalid_phone = df[
    df["phone"].astype(str).str.len() != 10
]

print(f"Invalid Phones: {len(invalid_phone)}")

# --------------------------------------------------
# Revenue Outlier Detection
# --------------------------------------------------

df["revenue"] = (
    df["price"].fillna(0)
    * df["quantity"]
)

top_revenue = df.nlargest(10, "revenue")[
    [
        "transaction_id",
        "product_id",
        "quantity",
        "price",
        "revenue"
    ]
]

print("\nTop Revenue Transactions:")
print(top_revenue)

print("\nBusiness Validation Audit Completed.")