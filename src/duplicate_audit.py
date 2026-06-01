import pandas as pd

FILE_PATH = "data/raw/USECASE - Data Engineering.xlsx"

# Load sheets
retail1 = pd.read_excel(FILE_PATH, sheet_name="retail_data1")
retail2 = pd.read_excel(FILE_PATH, sheet_name="retail_data2")

# Merge datasets
df = pd.concat([retail1, retail2], ignore_index=True)

print("=" * 60)
print("DUPLICATE TRANSACTION AUDIT")
print("=" * 60)

# Find duplicate transaction IDs
duplicates = df[df.duplicated(subset=["transaction_id"], keep=False)]

print(f"\nDuplicate Transaction Rows: {len(duplicates)}")

print("\nFirst 20 Duplicate Records:\n")

print(
    duplicates[
        [
            "transaction_id",
            "customer_id",
            "product_id",
            "quantity",
            "price"
        ]
    ]
    .sort_values("transaction_id")
    .head(20)
)

# Export duplicates
duplicates.to_csv(
    "outputs/duplicate_transactions.csv",
    index=False
)

print("\nDuplicate file exported successfully.")