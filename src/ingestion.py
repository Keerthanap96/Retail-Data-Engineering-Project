import pandas as pd
import os

FILE_PATH = "data/raw/USECASE - Data Engineering.xlsx"

print("=" * 50)
print("RETAIL DATA ENGINEERING PROJECT")
print("=" * 50)

# Load Excel file
excel_file = pd.ExcelFile(FILE_PATH)

# Display sheet names
print("\nAvailable Sheets:")
print(excel_file.sheet_names)

# Read each sheet
for sheet in excel_file.sheet_names:
    df = pd.read_excel(FILE_PATH, sheet_name=sheet)

    print(f"\nSheet Name: {sheet}")
    print(f"Rows: {df.shape[0]}")
    print(f"Columns: {df.shape[1]}")

print("\nData Ingestion Successful!")