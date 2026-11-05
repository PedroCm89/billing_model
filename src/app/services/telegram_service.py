
from pathlib import Path
from uuid import uuid4
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

    async def download_file(self, file_id: str, destination_dir: Path) -> Path:

        telegram_file = await self.bot.get_file(file_id)

        extension = Path(telegram_file.file_path).suffix
        filename = f"{uuid4()}{extension}"

        destination_dir.mkdir(parents=True, exist_ok=True)

        file_path = destination_dir / filename

        await telegram_file.download_to_drive(
            custom_path=file_path
        )

        return file_path


