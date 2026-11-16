from src.db import get_connection

c = get_connection()

print("=== DATABASE SCHEMAS ===")
print(c.execute("""
    SELECT schema_name
    FROM information_schema.schemata
    ORDER BY schema_name
""").df().to_string(index=False))

print("\n=== ALL TABLES ===")
print(c.execute("""
    SELECT table_schema, table_name
    FROM information_schema.tables
    ORDER BY table_schema, table_name
""").df().to_string(index=False))

c.close()
