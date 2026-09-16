from fastapi import FastAPI, status
#  uv run fastapi dev

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/health", status_code = status.HTTP_200_OK)
async def health_check():
    return {"status": "healthy"}