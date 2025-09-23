from fastapi import FastAPI
from routes import analyze
from core.limiter import limiter
from slowapi.errors import RateLimitExceeded
from fastapi.responses import PlainTextResponse
from core.config import settings

app = FastAPI(title=settings.PROJECT_NAME, version=settings.VERSION)

# Rate limiting
app.state.limiter = limiter
app.add_exception_handler(RateLimitExceeded, lambda request, exc: PlainTextResponse("Rate limit exceeded", status_code=429))

# Routers
app.include_router(analyze.router)