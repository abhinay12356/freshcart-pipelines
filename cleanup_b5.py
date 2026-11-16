from src.db import get_connection

c = get_connection()

c.execute("""
    DELETE FROM gold.orders
    WHERE order_id = 'MOCK-DQ-001'
""")

print("Mock record removed successfully.")
c.close()
