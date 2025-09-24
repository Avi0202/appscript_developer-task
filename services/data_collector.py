from ddgs import DDGS

def get_sector_news(sector: str, max_results: int = 5):  #if there are performance issues max results can be reduced, 
                                                        #in my testing token limit wasn't reached even with 10 results 
    results = []
    query = f"{sector} India market news"
    with DDGS() as dgs:
        for r in dgs.news(query, max_results=max_results):
            results.append({
                "title": r.get("title"),
                "snippet": r.get("body") or "",  
                "url": r.get("url")
            })
    return results