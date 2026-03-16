import requests
from database import SessionLocal
from models.customer import Customer

FLASK_URL = "http://mock-server:5000/api/customers"


def ingest_data():
    db = SessionLocal()

    page = 1
    limit = 50
    total_processed = 0

    while True:
        r = requests.get(f"{FLASK_URL}?page={page}&limit={limit}")
        data = r.json()

        customers = data["data"]

        if not customers:
            break

        for c in customers:
            existing = db.get(Customer, c["customer_id"])

            if existing:
                for k, v in c.items():
                    setattr(existing, k, v)
            else:
                db.add(Customer(**c))

            total_processed += 1

        db.commit()
        page += 1

    db.close()
    return total_processed