from src.db import get_connection

c = get_connection()

print("=== B4 BASELINE: CUST-02 HISTORY ===")
print(c.execute("""
    SELECT *
    FROM silver.customer_tier_history
    WHERE customer_id = 'CUST-02'
    ORDER BY valid_from
""").df().to_string(index=False))

print("\n=== B4 BASELINE: ORD-1002 ===")
print(c.execute("""
    SELECT order_id, customer_tier, amount_inr, loyalty_points
    FROM gold.orders
    WHERE order_id = 'ORD-1002'
""").df().to_string(index=False))

print("\n=== B4 BASELINE: GOLD TOTALS ===")
print(c.execute("""
    SELECT COUNT(*) AS gold_orders,
           SUM(loyalty_points) AS total_loyalty_points
    FROM gold.orders
""").df().to_string(index=False))

print("\n=== GOLD TABLE COLUMNS ===")
print(c.execute("PRAGMA table_info('gold.orders')").df().to_string(index=False))

c.close()
