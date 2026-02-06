from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

BASE = "/api/v1"

def test_health():
    r = client.get(f"{BASE}/health")
    assert r.status_code == 200
    assert r.json() == {"status": "ok"}

def test_predict_returns_number():
    payload = {
        "pickup_datetime": "2015-01-27 13:08:24 UTC",
        "pickup_longitude": -73.9851,
        "pickup_latitude": 40.7589,
        "dropoff_longitude": -73.9772,
        "dropoff_latitude": 40.7527,
        "passenger_count": 1
    }

    response = client.post(f"{BASE}/predict", json=payload)
    assert response.status_code == 200, response.text

    data = response.json()
    assert "fare_amount" in data
    assert isinstance(data["fare_amount"], (int, float))
