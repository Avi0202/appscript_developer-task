#as it was a single point api i went ahead with api key which can be changed in .env file, for complex apps oauth or jwt will be used
from fastapi import Security, HTTPException, status
from fastapi.security import APIKeyHeader
from core.config import settings



api_key_header = APIKeyHeader(name="X-API-KEY")

def get_api_key(api_key: str = Security(api_key_header)):
    if api_key != settings.API_KEY:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN, detail="Unauthorized or invalid API Key"
        )
    return api_key