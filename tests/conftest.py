import pytest
from fastapi.testclient import TestClient

from fastapi_zero.app import app


# Bloco de teste reutilizavel
@pytest.fixture
def client():
    return TestClient(app)
