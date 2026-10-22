from telegram import Bot
from app.core.config import settings

class TelegramService:
    def __init__(self):
        self.bot = Bot(token=settings.telegram_bot_token)

    async def check_connection(self):
            return await self.bot.get_me()

    async def send(self, chat_id: int, text: str):
        return await self.bot.send_message(
            chat_id=chat_id,
            text=text
            )