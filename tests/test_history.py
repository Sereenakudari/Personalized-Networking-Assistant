import httpx

def test_history():
    response = httpx.get("http://127.0.0.1:8000/history")

    assert response.status_code == 200
    assert isinstance(response.json(), list)