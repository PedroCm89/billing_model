from pydantic import BaseModel
from typing import Literal

class TelegramChat(BaseModel):
    id: int
    type: str

class TelegramPhotoSize(BaseModel):
    file_id: str
    file_unique_id: str
    width: int
    height: int

class TelegramMessage(BaseModel):
    message_id: int
    chat: TelegramChat
    text: str | None = None
    caption: str | None = None
    photo: list[TelegramPhotoSize] | None = None

class TelegramUpdate(BaseModel):
    update_id: int
    message: TelegramMessage | None=None

class TelegramMessageResult(BaseModel):
    chat_id: int | None = None
    message_type: Literal["text", "photo", "unknown"]
    text: str | None = None
    photo_file_id: str | None = None