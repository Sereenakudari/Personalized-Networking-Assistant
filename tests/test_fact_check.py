import httpx

def test_fact_check():

    response = httpx.get(
        "http://127.0.0.1:8000/fact-check",
        params={
            "query": "Python"
        }
    )

    assert response.status_code == 200

    data = response.json()

    assert "summary" in data
    assert "url" in data