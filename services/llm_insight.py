import google.generativeai as genai
from core.config import settings
from core.logger import logger

genai.configure(api_key=settings.GEMINI_API_KEY)

def generate_report(sector: str, news_items: list) -> str:
   
    headlines_text = "\n".join([
        f"- {item['title']} :: {item['snippet']} ({item['url']})" 
        for item in news_items
    ])

    prompt = f"""
You are a trade research assistant. Analyze the following recent news for the **{sector} sector in India**:

{headlines_text}

Generate a structured **Markdown Report** with the following sections:

# Market Analysis Report: {sector.capitalize()}

## Market Overview
(Summary of key trends)

## Trade Opportunities
- Bullet points

## Risks & Challenges
- Bullet points

## Outlook
(Predictive analysis in 2-3 sentences)

---
"""

    try:
        model = genai.GenerativeModel("gemini-2.5-flash")
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        logger.error(f"Gemini analysis failed: {e}", exc_info=True)
        fallback = f"""# Market Analysis Report: {sector.capitalize()}   

## Market Overview
Unable to fetch AI-driven analysis due to an error.

## Trade Opportunities
- Data temporarily unavailable

## Risks & Challenges
- Data temporarily unavailable

## Outlook
Please retry later when AI service is available.

---
"""
        return fallback   #gracefull error handeling :-)