from src.db import get_connection

c = get_connection()

print("=== GOLD RECORDS FOR B2 ===")
print(c.execute("""
    SELECT order_id, customer_name, customer_tier,
           amount, currency, amount_inr, loyalty_points
    FROM gold.orders
    WHERE order_id IN ('ORD-1001', 'ORD-1003', 'ORD-1005')
    ORDER BY order_id
""").df().to_string(index=False))

c.close()
