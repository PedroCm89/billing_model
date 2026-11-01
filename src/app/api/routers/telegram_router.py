import secrets
from app.core.config import settings
from fastapi import APIRouter, status, Header, HTTPException
from app.schemas.telegram_schema import TelegramUpdate



router = APIRouter(
    prefix="/webhook",
    tags=["Telegram"]
    )

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
            status_code=403,
            detail="Invalid webhook secret",
        )

    message = update.message

    return {
        "status": "received",
        "update_id": update.update_id,
        "chat_id": message.chat.id if message else None,
        "has_text": bool(message and message.text),
        "photo_count": len(message.photo or []) if message else 0,
    }
