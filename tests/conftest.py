import pytest
from fastapi.testclient import TestClient

from app.main import app


@pytest.fixture(scope='session')
def client():
    client_ = TestClient(app)
    yield client_
    del client_


