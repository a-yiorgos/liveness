from fastapi.testclient import TestClient
from app import app

client = TestClient(app)


def test_favicon():
    response = client.get("/favicon.ico")
    assert response.status_code == 200
    assert response.headers["content-type"].startswith("application/json")
    data = response.json()
    assert "favicon" in data


def test_healthz():
    response = client.get("/healthz")
    assert response.headers["content-type"].startswith("application/json")
    assert response.status_code in [200, 500]
    data = response.json()
    if response.status_code == 200:
        assert data == {"status": "ok"}
    else:
        assert data == {"detail": "Internal Server Error"}


def test_probes():
    for endpoint in ["/liveness/100", "/readiness/100", "/startup/100"]:
        response = client.get(endpoint)
        assert response.headers["content-type"].startswith("application/json")
        assert response.status_code == 500
        data = response.json()
        assert "detail" in data
        assert data["detail"].startswith("Internal Server Error")

    for endpoint in ["/liveness/0", "/readiness/0", "/startup/0"]:
        response = client.get(endpoint)
        assert response.headers["content-type"].startswith("application/json")
        assert response.status_code == 200
        data = response.json()
        assert "status" in data
        assert data["status"].startswith("ok")


def test_catch_all():
    response = client.get("/some/random/route")
    assert response.status_code == 200
    assert response.headers["content-type"].startswith("application/json")
    assert response.json() == {"status": "ok"}
