import pandas as pd
import sqlite3

USE_CLOUD = False

if USE_CLOUD:
    from s3_loader import load_from_s3
    df = load_from_s3()
else:
    df = pd.read_csv("data/curated/retail_master_curated.csv")

conn = sqlite3.connect("retail_agent/retail.db")

df.to_sql(
    "retail_sales",
    conn,
    if_exists="replace",
    index=False
)

conn.close()

print("Database Created Successfully!")