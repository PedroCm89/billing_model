import asyncio

from app.services.telegram_service import TelegramService


async def main():
    service = TelegramService()

    chat_id = 1642137298
    message = await service.send(
        chat_id=chat_id,
        text="¡Hola! Mensaje de prueba desde PIME."
    )

    print(f"Mensaje enviado. ID: {message.message_id}")


if __name__ == "__main__":
    asyncio.run(main())