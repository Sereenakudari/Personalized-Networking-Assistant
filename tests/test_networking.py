import httpx

def test_networking():

    response = httpx.get(
        "http://127.0.0.1:8000/networking-coach",
        params={
            "question": "How do I introduce myself?"
        },
        timeout=60.0
    )

    assert response.status_code == 200

    data = response.json()

    assert "advice" in data