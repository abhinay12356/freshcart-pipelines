from src.db import get_connection

c = get_connection()

print("Gold order count:",
      c.execute("SELECT COUNT(*) FROM gold.orders").fetchone()[0])

print("Mock record count:",
      c.execute("""
          SELECT COUNT(*)
          FROM gold.orders
          WHERE order_id = 'MOCK-DQ-001'
      """).fetchone()[0])

print(c.execute("""
    SELECT
        COUNT(*) AS gold_orders,
        SUM(amount_inr) AS total_revenue,
        SUM(loyalty_points) AS total_loyalty_points
    FROM gold.orders
""").df().to_string(index=False))

c.close()
