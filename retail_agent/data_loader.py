import pandas as pd

def load_data():
    df = pd.read_csv("data/curated/retail_master_curated.csv")
    return df