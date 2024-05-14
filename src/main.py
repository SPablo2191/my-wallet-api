from fastapi import FastAPI
import uvicorn

from src.config import settings as global_settings
from src.database import lifespan
from src.account.router import router as account_router

app = FastAPI(lifespan=lifespan)
app.title = "My Wallet API"
app.version = global_settings.version

app.include_router(
    router = account_router,
    prefix= f"/api/{global_settings.api_version}"
)
