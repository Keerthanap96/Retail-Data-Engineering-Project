from data_loader import load_data

df = load_data()

def top_5_products():
    return (
        df.groupby("product_name")["Revenue"]
        .sum()
        .sort_values(ascending=False)
        .head(5)
    )

def revenue_by_city():
    return (
        df.groupby("city")["Revenue"]
        .sum()
        .sort_values(ascending=False)
    )

def revenue_by_category():
    return (
        df.groupby("category")["Revenue"]
        .sum()
        .sort_values(ascending=False)
    )

def monthly_revenue():
    return (
        df.groupby("Month")["Revenue"]
        .sum()
        .sort_values(ascending=False)
    )

def top_customers():
    return (
        df.groupby("customer_name")["Revenue"]
        .sum()
        .sort_values(ascending=False)
        .head(10)
    )

def revenue_by_payment_method():
    return (
        df.groupby("payment_method")["Revenue"]
        .sum()
        .sort_values(ascending=False)
    )

def online_vs_offline():
    return (
        df.groupby("purchase_location")["Revenue"]
        .sum()
        .sort_values(ascending=False)
    )

def pending_payments():
    return df[df["payment_status"] != "successful"][
        ["transaction_id", "customer_name", "Revenue", "payment_status"]
    ]