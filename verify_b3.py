from src.db import get_connection

c = get_connection()

print("=== ORD-1006 AFTER VALIDATION ===")

print(c.execute("""
    SELECT
        order_id,
        source,
        rejection_reasons,
        record_status
    FROM quarantine.orders_rejected
    WHERE order_id = 'ORD-1006'
""").df().to_string(index=False))

c.close()
