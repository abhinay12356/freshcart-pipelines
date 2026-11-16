from src.db import get_connection

c = get_connection()

print("=== B4.6 IDEMPOTENCY VERIFICATION ===")

print("\n1. ARJUN SCD2 HISTORY")
print(c.execute("""
    SELECT customer_id, email, tier, valid_from, valid_to, is_current
    FROM silver.customer_tier_history
    WHERE customer_id = 'CUST-02'
    ORDER BY valid_from
""").df().to_string(index=False))

print("\n2. ARJUN SCD2 ROW COUNT")
print(c.execute("""
    SELECT COUNT(*)
    FROM silver.customer_tier_history
    WHERE customer_id = 'CUST-02'
""").fetchone()[0])

print("\n3. ORD-1002 GOLD RESULT")
print(c.execute("""
    SELECT order_id, customer_tier, amount_inr, loyalty_points
    FROM gold.orders
    WHERE order_id = 'ORD-1002'
""").df().to_string(index=False))

print("\n4. GOLD SUMMARY")
print(c.execute("""
    SELECT COUNT(*) AS gold_orders,
           SUM(amount_inr) AS total_revenue,
           SUM(loyalty_points) AS total_loyalty_points
    FROM gold.orders
""").df().to_string(index=False))

print("\n5. BRONZE ORDERS BY RUN")
print(c.execute("""
    SELECT run_id, COUNT(*) AS order_records
    FROM bronze.orders_raw
    WHERE source IN ('web', 'mobile')
    GROUP BY run_id
    ORDER BY run_id DESC
    LIMIT 5
""").df().to_string(index=False))

c.close()
