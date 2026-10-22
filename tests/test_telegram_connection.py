import asyncio

from app.services.telegram_service import TelegramService

async def main():
    service = TelegramService()
    bot = await service.check_connection()
    print (f"Connection is ok. Bot: @{bot.username}")

if __name__ == "__main__":
    asyncio.run(main())