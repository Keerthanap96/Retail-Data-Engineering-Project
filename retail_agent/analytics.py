from retail_queries import *

def run_query(user_query):

    query = user_query.lower()

    if "top product" in query:
        return top_5_products()

    elif "city" in query:
        return revenue_by_city()

    elif "category" in query:
        return revenue_by_category()

    elif "monthly" in query:
        return monthly_revenue()

    elif "customer" in query:
        return top_customers()

    elif "payment method" in query:
        return revenue_by_payment_method()

    elif "online" in query or "offline" in query:
        return online_vs_offline()

    elif "pending" in query:
        return pending_payments()

    else:
        return "Query not recognized."