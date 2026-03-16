import json
from flask import Flask, jsonify, request, abort

app = Flask(__name__)

with open("data/customers.json") as f:
    customers = json.load(f)


@app.route("/api/health")
def health():
    return {"status": "ok"}


@app.route("/api/customers")
def get_customers():
    page = int(request.args.get("page", 1))
    limit = int(request.args.get("limit", 10))

    start = (page - 1) * limit
    end = start + limit

    data = customers[start:end]

    return jsonify({
        "data": data,
        "total": len(customers),
        "page": page,
        "limit": limit
    })


@app.route("/api/customers/<cid>")
def get_customer(cid):
    for c in customers:
        if c["customer_id"] == cid:
            return jsonify(c)

    abort(404)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)