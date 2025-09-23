from fastapi import FastAPI, Response, HTTPException
from data_collector import get_sector_news
from analyzer import generate_report

app = FastAPI(
    title="Trade Opportunities API",
    description="Analyze Indian market sectors and generate trade opportunity markdown reports.",
    version="0.1.0",
)

@app.get("/analyze/{sector}")
async def analyze_sector(sector: str):
    """
    Fetch news for a given sector, analyze it, and return a markdown report.
    """

    # Step 1: Collect Data
    try:
        news_items = get_sector_news(sector)
        if not news_items:
            raise HTTPException(
                status_code=404, detail=f"No news found for sector: {sector}"
            )
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Data collection error: {str(e)}")

    # Step 2: Analyze and generate markdown report
    report = generate_report(sector, news_items)

    # Step 3: Return Markdown
    return Response(content=report, media_type="text/markdown")