from src.db import get_connection

c = get_connection()

print("=== CUST-02 SCD2 HISTORY AFTER CHANGE ===")
print(c.execute("""
    SELECT *
    FROM silver.customer_tier_history
    WHERE customer_id = 'CUST-02'
    ORDER BY valid_from
""").df().to_string(index=False))

print("\n=== ORD-1002 AFTER CHANGE ===")
print(c.execute("""
    SELECT order_id, customer_tier, amount_inr, loyalty_points
    FROM gold.orders
    WHERE order_id = 'ORD-1002'
""").df().to_string(index=False))

print("\n=== GOLD TOTALS AFTER CHANGE ===")
print(c.execute("""
    SELECT COUNT(*) AS gold_orders,
           SUM(amount_inr) AS total_revenue,
           SUM(loyalty_points) AS total_loyalty_points
    FROM gold.orders
""").df().to_string(index=False))

c.close()