
from unittest.mock import AsyncMock, MagicMock

import pytest

from app.services.telegram_service import TelegramService


@pytest.mark.asyncio
async def test_download_file(tmp_path):

    # Arrange
    telegram_service = TelegramService()

    file_id = "telegram-file-123"

    telegram_file = MagicMock()
    telegram_file.file_path = "photos/invoice.jpg"
    telegram_file.download_to_drive = AsyncMock()

    mock_bot = MagicMock()
    mock_bot.get_file = AsyncMock(return_value=telegram_file)

    telegram_service.bot = mock_bot

    destination_dir = tmp_path / "uploads"

    # Act
    result = await telegram_service.download_file(
        file_id=file_id,
        destination_dir=destination_dir
    )

    # Assert
    mock_bot.get_file.assert_awaited_once_with(file_id)

    telegram_file.download_to_drive.assert_awaited_once_with(
        custom_path=result
    )

    assert result.parent == destination_dir
    assert result.suffix == ".jpg"
    assert result.exists() is False
    assert destination_dir.exists()
