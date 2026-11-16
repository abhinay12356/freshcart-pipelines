from src.db import get_connection

c = get_connection()

print("=== DEDUPLICATED ORDERS ===")
result = c.execute("""
    SELECT *
    FROM silver.orders_deduplicated
    WHERE order_id IN ('ORD-1003', 'ORD-1005')
    ORDER BY order_id
""").df()

print(result.to_string(index=False))
c.close()
