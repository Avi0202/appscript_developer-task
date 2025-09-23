from duckduckgo_search import DDGS

def get_sector_news(sector: str, max_results: int = 5):
    results = []
    query = f"{sector} India market news"
    with DDGS() as ddgs:
        for r in ddgs.news(query, max_results=max_results):
            results.append({
                "title": r.get("title"),
                "snippet": r.get("body") or "",  
                "url": r.get("url")
            })
    return results