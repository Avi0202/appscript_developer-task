from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from slowapi.errors import RateLimitExceeded
from core.logger import logger
from core.config import settings
from core.limiter import limiter
from routes import analyze

app = FastAPI(title=settings.PROJECT_NAME, version=settings.VERSION)

# Attach limiter
app.state.limiter = limiter
app.add_exception_handler(RateLimitExceeded, lambda request, exc: JSONResponse({"error": "Rate limit exceeded"}, status_code=429))

# Global exception handler
@app.middleware("http")
async def log_requests(request: Request, call_next):
    logger.info(f"Incoming request: {request.method} {request.url}")
    try:
        response = await call_next(request)
        logger.info(f"Response status: {response.status_code}")
        return response
    except Exception as e:
        logger.error(f"Exception: {str(e)}", exc_info=True)
        return JSONResponse(status_code=500, content={"error": "Internal server error. Please try again later."})

# Include routes
app.include_router(analyze.router)