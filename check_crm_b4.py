from src.db import get_connection

c = get_connection()

print(c.execute("""
    SELECT ingest_seq, run_id, raw_json
    FROM bronze.customers_raw
    ORDER BY ingest_seq DESC
    LIMIT 10
""").df().to_string(index=False))

c.close()
