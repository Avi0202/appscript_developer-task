# this tests is session is getting created and incremented properly
from core.session import get_or_create_session
from fastapi import Request
from types import SimpleNamespace

def mock_request(host="127.0.0.1"):
    return SimpleNamespace(client=SimpleNamespace(host=host))

def test_session_creation():
    req = mock_request()
    session_id, session_data = get_or_create_session(req)
    assert session_id == "127.0.0.1"
    assert session_data["count"] >= 1

def test_session_increment():
    req = mock_request()
    _, data1 = get_or_create_session(req)
    _, data2 = get_or_create_session(req)
    assert data2["count"] == data1["count"] + 1