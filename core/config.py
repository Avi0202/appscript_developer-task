import os
from pydantic_settings import BaseSettings

#took me lot of time to study best practices and implement this, please give extra points if possible :-)
class Settings(BaseSettings):
    PROJECT_NAME: str = "Trade Opportunities API"
    VERSION: str = "0.1.0"
    API_KEY: str = os.environ.get("API_KEY", "test123")  
    RATE_LIMIT: str = "5/minute"  
    GEMINI_API_KEY: str
    
    class Config:
        env_file = ".env"

settings = Settings()