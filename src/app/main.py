from fastapi import FastAPI
from app.api.routers.endpoint import router as endpoint_router
from app.api.routers.telegram_router import router as telegram_router
#  uv run fastapi dev

app = FastAPI()
app.include_router(endpoint_router)
app.include_router(telegram_router)