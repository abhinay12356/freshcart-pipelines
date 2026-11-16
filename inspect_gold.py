from src.db import get_connection

c = get_connection()
print(c.execute("DESCRIBE gold.orders").df().to_string(index=False))
c.close()
