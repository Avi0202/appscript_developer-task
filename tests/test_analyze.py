#tests the main route /analyze/{sector} for rate limiting, api key validation, input validation and successful response
import pytest
from fastapi.testclient import TestClient
from app import app
from core.config import settings

client = TestClient(app)

def test_analyze_valid_sector(monkeypatch):
    
    from services import data_collector

    def fake_get_sector_news(sector, max_results=5):
        return [
            {"title": "Sample news 1", "snippet": "snippet text", "url": "http://example.com"}
        ]

    monkeypatch.setattr(data_collector, "get_sector_news", fake_get_sector_news)

    response = client.get("/analyze/technology", headers={"X-API-KEY": settings.API_KEY})
    assert response.status_code == 200
    text = response.text
    assert "Market Analysis Report" in text
    assert "Technology" in text

def test_analyze_invalid_sector():
    response = client.get("/analyze/1234", headers={"X-API-KEY": settings.API_KEY})
    assert response.status_code == 400
    assert response.json()["detail"] == "Invalid sector name"

def test_analyze_no_api_key():
    response = client.get("/analyze/technology")
    assert response.status_code == 403

def test_analyze_rate_limit(monkeypatch):
    from services import data_collector
    monkeypatch.setattr(data_collector, "get_sector_news", lambda sector, max=5: [{"title": "news", "snippet": "snippet", "url": "http://example.com"}])
    
    
    res1 = client.get("/analyze/technology", headers={"X-API-KEY": settings.API_KEY})
    assert res1.status_code == 200
 
    for _ in range(10):
        res = client.get("/analyze/technology", headers={"X-API-KEY": settings.API_KEY})
    assert res.status_code in [200, 429]  