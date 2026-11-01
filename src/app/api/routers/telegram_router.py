import secrets
from app.core.config import settings
from fastapi import APIRouter, status, Header, HTTPException
from app.schemas.telegram_schema import TelegramUpdate
from app.services.telegram_update_service import TelegramUpdateService



router = APIRouter(
    prefix="/webhook",
    tags=["Telegram"]
    )
telegram_update_service = TelegramUpdateService()

@router.post("/telegram", status_code= status.HTTP_200_OK,)
async def telegram_webhook(
    update: TelegramUpdate,
    x_telegram_bot_api_secret_token: str | None = Header(
        default=None,
        alias="X-Telegram-Bot-Api-Secret-Token",
    ),
):
    if (
        x_telegram_bot_api_secret_token is None
        or not secrets.compare_digest(
            x_telegram_bot_api_secret_token,
            settings.telegram_webhook_secret,
        )
    ):
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Invalid webhook secret",
        )

    result = telegram_update_service.process_update(update)

    return {
        "status": "received",
        "update_id": update.update_id,
        **result.model_dump(),
    }
