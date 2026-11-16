from src.db import get_connection

c = get_connection()

c.execute("""
    INSERT INTO gold.orders (
        order_id,
        customer_email,
        customer_name,
        order_date,
        amount,
        currency,
        pincode,
        updated_at,
        customer_tier,
        rate_to_inr,
        city,
        state,
        amount_inr,
        loyalty_points
    )
    VALUES (
        'MOCK-DQ-001',
        'mock@example.com',
        'Mock Customer',
        DATE '2026-09-05',
        100.00,
        'INR',
        '600041',
        TIMESTAMP '2026-09-05 10:00:00',
        'Silver',
        1.0000,
        'Chennai',
        'Tamil Nadu',
        NULL,
        1
    )
""")

print("Mock record inserted successfully.")
c.close()
