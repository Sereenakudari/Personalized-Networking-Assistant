from fastapi.testclient import TestClient
from backend.main import app

client = TestClient(app)

def test_fact_check():
    response = client.get(
        "/fact-check",
        params={"query": "Python"}
    )

    assert response.status_code == 200