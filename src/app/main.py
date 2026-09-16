from fastapi import FastAPI

#  uv run fastapi dev

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}