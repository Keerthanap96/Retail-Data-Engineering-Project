def generate_sql(question):

    question = question.lower()

    if "revenue by city" in question:
        return """
        SELECT city,
               SUM(Revenue) AS Revenue
        FROM retail_sales
        GROUP BY city
        ORDER BY Revenue DESC
        """

    elif "revenue by category" in question:
        return """
        SELECT category,
               SUM(Revenue) AS Revenue
        FROM retail_sales
        GROUP BY category
        ORDER BY Revenue DESC
        """

    elif "top customers" in question:
        return """
        SELECT customer_name,
               SUM(Revenue) AS Revenue
        FROM retail_sales
        GROUP BY customer_name
        ORDER BY Revenue DESC
        LIMIT 10
        """

    elif "top products" in question:
        return """
        SELECT product_name,
               SUM(Revenue) AS Revenue
        FROM retail_sales
        GROUP BY product_name
        ORDER BY Revenue DESC
        LIMIT 10
        """

    elif "revenue by payment method" in question:
        return """
        SELECT payment_method,
               SUM(Revenue) AS Revenue
        FROM retail_sales
        GROUP BY payment_method
        ORDER BY Revenue DESC
        """

    elif "monthly revenue" in question:
        return """
        SELECT Month,
               SUM(Revenue) AS Revenue
        FROM retail_sales
        GROUP BY Month
        """

    elif "pending payments" in question:
        return """
        SELECT payment_status,
               COUNT(*) AS Transactions
        FROM retail_sales
        WHERE payment_status='Pending'
        GROUP BY payment_status
        """

    return None