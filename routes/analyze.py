from fastapi import APIRouter, Depends, Response, Request
from core.config import settings
from core.auth import get_api_key
from core.security import validate_sector
from core.limiter import limiter
from core.session import get_or_create_session
from services.data_collector import get_sector_news
from services.analyzer import generate_report

router = APIRouter()

@router.get("/analyze/{sector}")
@limiter.limit(settings.RATE_LIMIT)  
async def analyze_sector(
    request: Request,
    sector: str,
    api_key: str = Depends(get_api_key)
):
    
    session_id, session_data = get_or_create_session(request)

   
    sector = validate_sector(sector)

    
    news_items = get_sector_news(sector)
    if not news_items:
        return Response(content=f"# No News Found for {sector}", media_type="text/markdown")

    
    report = generate_report(sector, news_items)

    return Response(content=report, media_type="text/markdown")