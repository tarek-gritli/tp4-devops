import pytest

from app import app
from main import main


@pytest.fixture
def client():
    app.config["TESTING"] = True
    return app.test_client()


def test_hello(client):
    r = client.get("/")
    assert r.status_code == 200
    assert b"ok" in r.data


def test_main(capsys):
    main()
    captured = capsys.readouterr()
    assert "Hello from tp4!" in captured.out
