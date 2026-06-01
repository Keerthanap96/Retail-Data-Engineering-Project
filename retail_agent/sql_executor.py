import sqlite3
import pandas as pd


def run_sql(query):

    conn = sqlite3.connect("retail_agent/retail.db")

    result = pd.read_sql_query(
        query,
        conn
    )

    conn.close()

    return result