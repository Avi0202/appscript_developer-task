import os
from pydantic import BaseSettings

class Settings(BaseSettings):
    PROJECT_NAME: str = "Trade Opportunities API"
    VERSION: str = "0.1.0"
    API_KEY: str = os.environ.get("API_KEY", "test123")  
    RATE_LIMIT: str = "5/minute"  

settings = Settings()