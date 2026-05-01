import pytest

from app import app


@pytest.fixture
def client():
    app.config["TESTING"] = True
    return app.test_client()


def test_hello(client):
    r = client.get("/")
    assert r.status_code == 200
    assert b"ok" in r.data
