from src.db import get_connection

c = get_connection()

print(c.execute("""
    SELECT table_schema, table_name
    FROM information_schema.tables
    WHERE lower(table_name) LIKE '%gold%'
       OR lower(table_name) LIKE '%orders%'
    ORDER BY table_schema, table_name
""").df().to_string(index=False))

c.close()
