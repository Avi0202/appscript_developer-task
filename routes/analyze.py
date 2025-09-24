from fastapi import APIRouter, Depends, Response, Request
from core.config import settings
from core.auth import get_api_key
from core.validation import validate_sector
from core.limiter import limiter
from core.session import get_or_create_session
from services.data_collector import get_sector_news
from services.llm_insight import generate_report

router = APIRouter()

@router.get("/analyze/{sector}")
@limiter.limit(settings.RATE_LIMIT)  
async def analyze_sector(
    request: Request,
    sector: str,
    api_key: str = Depends(get_api_key)   # API key is only used for validation for now. Can be used for advanvced features like per-key rate limiting etc.
):
    
    session_id, session_data = get_or_create_session(request) #session tracking, not currntly used for anything .I added it due to product requirement

   
    sector = validate_sector(sector)   #input is getting validated here, just checking for alphabets,validation can be updated to have specific list of sectors if needed

    
    news_items = get_sector_news(sector)  #fetching news from duckduckgo, list of dictionarys with title,snippet and url
    
    if not news_items:
        return Response(content=f"# No News Found for {sector}", media_type="text/markdown")

    
    report = generate_report(sector, news_items)   #llm call to generate mardown report

    return Response(content=report, media_type="text/markdown")