from app.schemas.telegram_schema import (TelegramUpdate, TelegramMessageResult)

class TelegramUpdateService:

    def process_update(self, update: TelegramUpdate)-> TelegramMessageResult:
        message = update.message

        if message is None:
            return TelegramMessageResult(message_type="unknown")

        if message.photo:
            return TelegramMessageResult(
                chat_id=message.chat.id,
                message_type="photo",
                text=message.caption,
                photo_file_id=message.photo[-1].file_id,
            )

        if message.text:
            return TelegramMessageResult(
                chat_id=message.chat.id,
                message_type="text",
                text= message.text,
            )

        return TelegramMessageResult(
            chat_id=message.chat.id,
            message_type="unknown",
        )
    