from src.db import get_connection

c = get_connection()

print("=== GOLD SUMMARY AFTER B3 ===")

print(c.execute("""
    SELECT
        COUNT(*) AS total_orders,
        SUM(amount_inr) AS total_revenue,
        SUM(loyalty_points) AS total_loyalty_points
    FROM gold.orders
""").df().to_string(index=False))

c.close()
