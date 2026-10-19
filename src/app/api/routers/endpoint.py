from fastapi import APIRouter,status

router = APIRouter(tags=["endpoint"])

@router.get("/health", status_code = status.HTTP_200_OK)
async def health_check():
    return {"status": "healthy"}

@router.get("/")
async def root():
    return {"message": "Hello World"}