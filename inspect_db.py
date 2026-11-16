from src.db import get_connection

conn = get_connection()

queries = {
    "CUSTOMER TIER HISTORY": "SELECT * FROM silver.customer_tier_history",
    "ORD-1002 ORDER": """
        SELECT *
        FROM silver.orders_deduplicated
        WHERE order_id = 'ORD-1002'
    """,
    "GOLD ORDERS": """
        SELECT order_id, customer_name, customer_tier,
               amount_inr, loyalty_points
        FROM gold.orders
        ORDER BY order_id
    """
}

for title, query in queries.items():
    print("\n========== " + title + " ==========")
    print(conn.execute(query).df().to_string(index=False))

conn.close()
