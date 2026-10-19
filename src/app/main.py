from fastapi import FastAPI
from app.api.routers.endpoint import router
#  uv run fastapi dev

app = FastAPI()
app.include_router(router)