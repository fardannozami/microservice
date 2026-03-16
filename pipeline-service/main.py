from fastapi import FastAPI, HTTPException
from database import Base, engine, SessionLocal
from models.customer import Customer
from services.ingestion import ingest_data

app = FastAPI()

Base.metadata.create_all(bind=engine)


@app.post("/api/ingest")
def ingest():
    count = ingest_data()
    return {"status": "success", "records_processed": count}


@app.get("/api/customers")
def get_customers(page: int = 1, limit: int = 10):
    db = SessionLocal()

    start = (page - 1) * limit

    customers = db.query(Customer).offset(start).limit(limit).all()
    total = db.query(Customer).count()

    db.close()

    return {
        "data": customers,
        "total": total,
        "page": page,
        "limit": limit
    }


@app.get("/api/customers/{customer_id}")
def get_customer(customer_id: str):
    db = SessionLocal()

    customer = db.get(Customer, customer_id)

    if not customer:
        raise HTTPException(status_code=404)

    return customer