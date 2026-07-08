import httpx

def test_event():

    response = httpx.post(
        "http://127.0.0.1:8000/event-copilot",
        json={
            "prompt": "I am attending an AI conference."
        },
        timeout=60.0
    )

    assert response.status_code == 200

    data = response.json()

    assert "response" in data