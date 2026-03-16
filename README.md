# Microservice Project

A Python microservice project with a FastAPI pipeline service and a Flask mock server.

## Project Structure

```
microservice/
├── pipeline-service/       # FastAPI service
│   ├── main.py             # API endpoints
│   ├── database.py         # SQLAlchemy configuration
│   ├── models/
│   │   └── customer.py     # Customer model
│   └── services/
│       └── ingestion.py    # Data ingestion service
└── mock-server/            # Flask mock server
    └── app.py              # Mock API endpoints
```

## Requirements

- Python 3.8+
- FastAPI
- SQLAlchemy
- Flask
- requests

## Environment Variables

Set `DATABASE_URL` for the pipeline service (e.g., `sqlite:///customers.db`).

## Running the Services

### Mock Server

```bash
cd mock-server
python app.py
```

The mock server runs on `http://localhost:5000`.

### Pipeline Service

```bash
cd pipeline-service
pip install fastapi uvicorn sqlalchemy requests
uvicorn main:app --reload
```

The API runs on `http://localhost:8000`.

## API Endpoints

### POST /api/ingest
Ingest customer data from the mock server.

### GET /api/customers
List customers with pagination.

Query parameters:
- `page` (int): Page number (default: 1)
- `limit` (int): Items per page (default: 10)

### GET /api/customers/{customer_id}
Get a specific customer by ID.
