from fastapi import FastAPI


from src.config import settings as global_settings
from src.database import lifespan
from src.account.router import router as account_router
from src.movement.router import router as movement_router

app = FastAPI(lifespan=lifespan)
app.title = "My Wallet API"
app.version = global_settings.version

app.include_router(
    router = account_router,
    prefix= f"/api/{global_settings.api_version}"
)
app.include_router(
    router = movement_router,
    prefix= f"/api/{global_settings.api_version}"
)