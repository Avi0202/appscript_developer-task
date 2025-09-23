Setup Instructions

1. Clone Repository

  git clone https://github.com/Avi0202/appscript_developer-task.git
  cd trade-opportunities-api

2. Create Virtual Environment

  python -m venv venv  
  - Linux Mac        
    source venv/bin/activate
  - Windows
    venv\Scripts\activate        

3. Install Dependencies

  pip install -r requirements.txt

4. Create .env File in Project Root

  API_KEY=test123         (API key for security can be set here)
  RATE_LIMIT=5/minute
  GEMINI_API_KEY=your_google_gemini_api_key_here

5. Run the Server

  uvicorn app:app --reload

The API will be available at:
http://127.0.0.1:8000

Interactive docs:
http://127.0.0.1:8000/docs