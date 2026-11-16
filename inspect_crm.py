from src.db import get_connection

conn = get_connection()

print("========== ARJUN CRM RAW RECORDS ==========")
rows = conn.execute("""
    SELECT ingest_seq, run_id, extracted_at, raw_json
    FROM bronze.customers_raw
    WHERE LOWER(raw_json) LIKE '%arjun%'
    ORDER BY ingest_seq
""").df()

print(rows.to_string(index=False))

conn.close()
