from src.db import get_connection

c = get_connection()

print("=== QUARANTINE SUMMARY ===")

print(c.execute("""
    SELECT order_id, rejection_reasons
    FROM quarantine.orders_rejected
    ORDER BY order_id
""").df().to_string(index=False))

print("\nTotal quarantined orders:")
print(c.execute("""
    SELECT COUNT(*) FROM quarantine.orders_rejected
""").fetchone()[0])

c.close()
