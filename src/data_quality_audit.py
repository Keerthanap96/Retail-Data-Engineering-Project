import pandas as pd

FILE_PATH = "data/raw/USECASE - Data Engineering.xlsx"

# Load sheets
retail1 = pd.read_excel(FILE_PATH, sheet_name="retail_data1")
retail2 = pd.read_excel(FILE_PATH, sheet_name="retail_data2")

# Merge datasets
df = pd.concat([retail1, retail2], ignore_index=True)

print("=" * 60)
print("DATA QUALITY AUDIT REPORT")
print("=" * 60)

# 1. Missing Prices
missing_prices = df["price"].isnull().sum()
print(f"\nMissing Prices: {missing_prices}")

# 2. Negative Quantities
negative_qty = (df["quantity"] <= 0).sum()
print(f"Negative Quantities: {negative_qty}")

# 3. Duplicate Transaction IDs
duplicate_txns = df["transaction_id"].duplicated().sum()
print(f"Duplicate Transaction IDs: {duplicate_txns}")

# 4. Unique Categories
print("\nUnique Categories:")
print(sorted(df["category"].astype(str).unique()))

# 5. Unique Product Names
print("\nSample Product Names:")
print(sorted(df["product_name"].astype(str).unique())[:20])

# 6. Date Type Check
print("\nTransaction Date Data Type:")
print(df["transaction_date"].dtype)

print("\nAudit Completed Successfully.")