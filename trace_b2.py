from src.db import get_connection

c = get_connection()

print("=== SILVER CLEANED ===")
print(c.execute("""
    SELECT *
    FROM silver.orders_clean
    WHERE order_id IN ('ORD-1003', 'ORD-1005')
    ORDER BY order_id, updated_at
""").df().to_string(index=False))

print("\n=== DEDUPLICATED ===")
print(c.execute("""
    SELECT *
    FROM silver.orders_deduplicated
    WHERE order_id IN ('ORD-1003', 'ORD-1005')
    ORDER BY order_id
""").df().to_string(index=False))

c.close()
