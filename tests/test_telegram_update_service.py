from app.services.telegram_update_service import TelegramUpdateService
from app.schemas.telegram_schema import TelegramUpdate

def test_process_update_without_message():

    #Arramge

    service = TelegramUpdateService()
    update = TelegramUpdate(update_id=1)

    #Act

    result = service.process_update(update)

    #Assert

    assert result.message_type == "unknown"
    assert result.chat_id is None

def test_process_update_with_text():

    #Arrange
    service = TelegramUpdateService()

    update = TelegramUpdate(
        update_id=2,
        message={
            "message_id":10,
            "chat":{
                "id":123456,
                "type":"private"
            },
            "text":"Hola quiero una factura"
        },
    )
    #Act
    result = service.process_update(update)

    #Assert

    assert result.message_type == "text"
    assert result.chat_id == 123456
    assert result.text == "Hola quiero una factura"
    assert result.photo_file_id is None


def test_process_update_with_photo():

    # Arrange
    service = TelegramUpdateService()

    update = TelegramUpdate(
        update_id=3,
        message={
            "message_id": 11,
            "chat": {
                "id": 123456,
                "type": "private",
            },
            "photo": [
                {
                    "file_id": "photo_small",
                    "file_unique_id": "unique_small",
                    "width": 90,
                    "height": 90,
                },
                {
                    "file_id": "photo_medium",
                    "file_unique_id": "unique_medium",
                    "width": 320,
                    "height": 320,
                },
                {
                    "file_id": "photo_large",
                    "file_unique_id": "unique_large",
                    "width": 1280,
                    "height": 1280,
                },
            ],
        },
    )

    # Act
    result = service.process_update(update)

    # Assert
    assert result.message_type == "photo"
    assert result.chat_id == 123456
    assert result.photo_file_id == "photo_large"
    assert result.text is None

    
def test_process_update_with_photo_and_caption():

    # Arrange
    service = TelegramUpdateService()

    update = TelegramUpdate(
        update_id=4,
        message={
            "message_id": 12,
            "chat": {
                "id": 123456,
                "type": "private",
            },
            "caption": "Factura del proveedor de materiales",
            "photo": [
                {
                    "file_id": "photo_small",
                    "file_unique_id": "unique_small",
                    "width": 90,
                    "height": 90,
                },
                {
                    "file_id": "photo_large",
                    "file_unique_id": "unique_large",
                    "width": 1280,
                    "height": 1280,
                },
            ],
        },
    )

    # Act
    result = service.process_update(update)

    # Assert
    assert result.message_type == "photo"
    assert result.chat_id == 123456
    assert result.photo_file_id == "photo_large"
    assert result.text == "Factura del proveedor de materiales"


def test_process_update_with_unsupported_message():

    # Arrange
    service = TelegramUpdateService()

    update = TelegramUpdate(
        update_id=5,
        message={
            "message_id": 13,
            "chat": {
                "id": 123456,
                "type": "private",
            },
            "sticker": {
                "file_id": "sticker_file_id",
                "file_unique_id": "sticker_unique_id",
                "type": "regular",
            },
        },
    )

    # Act
    result = service.process_update(update)

    # Assert
    assert result.message_type == "unknown"
    assert result.chat_id == 123456
    assert result.text is None
    assert result.photo_file_id is None

