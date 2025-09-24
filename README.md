
 

This project is a FastAPI service that fetches real-world market news for different sectors in India (e.g. technology, pharmaceuticals, agriculture), runs the data through Google’s Gemini LLM, and returns a **structured markdown report**. The report is intentionally markdown so it can be saved directly as `.md` and opened in any editor.  



---

## Features  

- **Single endpoint:** `GET /analyze/{sector}`  
  Example: `/analyze/technology`  
- **Real news data:** pulled from DuckDuckGo search (titles + snippets).  
- **AI analysis:** prompts Gemini to generate a markdown report with 4 consistent sections:
  - Market Overview  
  - Trade Opportunities  
  - Risks & Challenges  
  - Outlook  
- **Markdown output:** you can save the response as `report.md`.  
- **Security built-in:**  
  - Requires API Key (`X-API-KEY`)  
  - Input validation (only alphabetic sectors)  
  - Rate limiting (default: 5 requests/minute per client)  
- **Session tracking:** basic in-memory session per client (extendable later).  
- **Graceful fallbacks:** if the news API or Gemini fails, you still get a markdown file (with a fallback message instead of an error).  

---

## Project Structure

The project is organized into clear layers:

- `core/` → cross-cutting concerns like config, auth, logging, sessions,input validation
- `routes/` → only defines API endpoints, thin controller layer
- `services/` → handles business logic (fetching news, analyzing with LLM)
- `tests/` → pytest-based automated tests for endpoint, validation, session, and LLM behavior

```
appscript_developer-task/
├── app.py                         # FastAPI entrypoint, global middleware, exception handling
├── .env                           # Environment variables (API keys, configs) [ignored in Git]
├── requirements.txt               # Python dependencies
├── requirements-dev.txt           # Pyton dependencies for testing
├── README.md                      # Project documentation
│
├── core/                          # Cross-cutting core functionality
│   ├── config.py                  # Application settings (loads from .env using Pydantic Settings)
│   ├── auth.py                    # API Key authentication logic
│   ├── limiter.py                 # Rate limiting configuration (slowapi)
│   ├── logger.py                  # Centralized logging setup
│   ├── session.py                 # Lightweight in-memory session management
│   └── validation.py              # Regex validation for sector names
│
├── routes/                        # API route definitions
│   └── analyze.py                 # /analyze/{sector} endpoint
│
├── services/                      # Business logic (data fetch + AI analysis)
│   ├── data_collector.py          # Fetches live news data 
│   └── llm_insight.py             # Calls Gemini LLM to generate structured Markdown reports
│
└── tests/                         # Automated testing (pytest)
    ├── test_analyze.py            # Endpoint tests (valid input, invalid, rate limit, auth)
    ├── test_validation.py         # Unit tests for input validator
    └── test_session.py            # Session store behavior (creation, increment)
                 
```

## Setup  

1. **Clone the repo**  
   ```
   git clone https://github.com/Avi0202/appscript_developer-task.git
   cd appscript_developer-task
   ```

2. **Create a virtual environment**  
   ```
   python -m venv venv
   source venv/bin/activate   # Mac / Linux
   venv\Scripts\activate      # Windows
   ```

3. **Install dependencies**  
   ```
   pip install -r requirements.txt
   ```

4. **Set up `.env`** (put this file in the project root)  
   ```ini
   API_KEY=test123             # request must send it as X-API-KEY
   RATE_LIMIT=5/minute         # reduce it for testing rate limit per session implementation
   GEMINI_API_KEY=your_gemini_api_key_here
   ```

5. **Run locally**  
   ```bash
   uvicorn app:app --reload
   ```  
   Server should be up on `http://127.0.0.1:8000`  

   API docs here: `http://127.0.0.1:8000/docs`  

---

## Usage  

Every request needs the API key header:  

```
X-API-KEY: test123
```

Example (cURL):  

```
curl -H "X-API-KEY: test123" http://127.0.0.1:8000/analyze/technology
```

## Running Tests

Install dependencies
```
pip install -r requirements-dev.txt

```
Run pytest
```
pytest -v

```
 








