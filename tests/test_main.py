# tests/test_main.py
import pytest
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_addition():
    """
    Test case for valid addition request.
    """
    response = client.post("/add", json={"batchid": "id0101", "payload": [[1, 2], [3, 4]]})
    assert response.status_code == 200
    assert response.json()["response"] == [3, 7]

def test_invalid_payload():
    """
    Test case for invalid payload (non-list item in payload).
    Expects a 422 Unprocessable Entity status.
    """
    response = client.post("/add", json={"batchid": "id0102", "payload": [[1, 2], "invalid"]})
    assert response.status_code == 422

def test_empty_payload():
    """
    Test case for empty payload.
    Expects a 200 OK status with an empty response list.
    """
    response = client.post("/add", json={"batchid": "id0103", "payload": []})
    assert response.status_code == 200
    assert response.json()["response"] == []
