import pandas as pd

FILE_PATH = "data/raw/USECASE - Data Engineering.xlsx"

print("=" * 60)
print("DATA CLEANING PIPELINE")
print("=" * 60)

# Load sheets
products = pd.read_excel(FILE_PATH, sheet_name="product_details")
retail1 = pd.read_excel(FILE_PATH, sheet_name="retail_data1")
retail2 = pd.read_excel(FILE_PATH, sheet_name="retail_data2")

# Merge datasets
df = pd.concat([retail1, retail2], ignore_index=True)

original_rows = len(df)

print(f"\nOriginal Rows: {original_rows}")

# --------------------------------------------------
# Fix Missing Prices
# --------------------------------------------------

missing_before = df["price"].isnull().sum()

price_lookup = dict(
    zip(products["product_id"], products["price"])
)

df["price"] = df.apply(
    lambda row:
    price_lookup.get(row["product_id"])
    if pd.isnull(row["price"])
    else row["price"],
    axis=1
)

missing_after = df["price"].isnull().sum()

# --------------------------------------------------
# Remove Negative Quantities
# --------------------------------------------------

negative_rows = (df["quantity"] <= 0).sum()

df = df[df["quantity"] > 0]

# --------------------------------------------------
# Remove Duplicate Transactions
# --------------------------------------------------

before_duplicates = len(df)

df = df.drop_duplicates(
    subset=["transaction_id"],
    keep="first"
)

after_duplicates = len(df)

duplicate_removed = before_duplicates - after_duplicates

# --------------------------------------------------
# Standardize Categories
# --------------------------------------------------

category_map = {
    "ELEC": "Electronics",
    "electronics": "Electronics",

    "FURN": "Furniture",
    "furniture": "Furniture",

    "CLOTH": "Clothing",
    "clothing": "Clothing",

    "HOME": "Home Appliances",
    "home appliances": "Home Appliances"
}

df["category"] = df["category"].replace(category_map)

# --------------------------------------------------
# Standardize Product Names
# --------------------------------------------------

df["product_name"] = df["product_name"].str.title()

df["product_name"] = df["product_name"].replace({
    "Tv": "TV"
})

# --------------------------------------------------
# Convert Dates
# --------------------------------------------------

df["transaction_date"] = pd.to_datetime(
    df["transaction_date"],
    errors="coerce"
)

# --------------------------------------------------
# Mask Email
# --------------------------------------------------

def mask_email(email):
    email = str(email)

    if "@" not in email:
        return email

    name, domain = email.split("@")

    return name[:2] + "***@" + domain


df["email_masked"] = df["email"].apply(mask_email)

# --------------------------------------------------
# Mask Phone
# --------------------------------------------------

def mask_phone(phone):
    phone = str(phone)

    if len(phone) < 4:
        return phone

    return phone[:2] + "******" + phone[-2:]


df["phone_masked"] = df["phone"].apply(mask_phone)

# --------------------------------------------------
# Save Clean Dataset
# --------------------------------------------------

df.to_csv(
    "data/processed/retail_master_cleaned.csv",
    index=False
)

# --------------------------------------------------
# Cleaning Summary
# --------------------------------------------------

summary = pd.DataFrame({
    "Metric": [
        "Original Rows",
        "Missing Prices Before",
        "Missing Prices After",
        "Negative Rows Removed",
        "Duplicate Rows Removed",
        "Final Rows"
    ],
    "Value": [
        original_rows,
        missing_before,
        missing_after,
        negative_rows,
        duplicate_removed,
        len(df)
    ]
})

summary.to_csv(
    "outputs/cleaning_summary.csv",
    index=False
)

print("\nCleaning Completed Successfully!")

print(f"Missing Prices Fixed: {missing_before}")
print(f"Negative Rows Removed: {negative_rows}")
print(f"Duplicate Rows Removed: {duplicate_removed}")
print(f"Final Rows: {len(df)}")