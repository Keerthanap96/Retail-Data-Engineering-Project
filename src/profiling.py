import pandas as pd

FILE_PATH = "data/raw/USECASE - Data Engineering.xlsx"

sheets = ["product_details", "retail_data1", "retail_data2"]

for sheet in sheets:

    print("\n" + "=" * 70)
    print(f"PROFILE REPORT : {sheet}")
    print("=" * 70)

    df = pd.read_excel(FILE_PATH, sheet_name=sheet)

    print("\nShape:")
    print(df.shape)

    print("\nColumns:")
    print(df.columns.tolist())

    print("\nData Types:")
    print(df.dtypes)

    print("\nMissing Values:")
    print(df.isnull().sum())

    print("\nDuplicate Rows:")
    print(df.duplicated().sum())