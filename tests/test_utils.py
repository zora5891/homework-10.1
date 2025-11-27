from unittest.mock import mock_open, patch

import pytest

from src.utils import load_transactions


@pytest.mark.parametrize(
    "file_content,expected",
    [
        ("[]", []),
        ('{"key": "value"}', []),
        ('[{"id": 1}]', [{"id": 1}]),
    ],
)
def test_load_transactions(file_content, expected):
    """Проверка корректности загрузки JSON - файла"""
    with patch("builtins.open", mock_open(read_data=file_content)):
        assert load_transactions("dummy.json") == expected


def test_load_transactions_file_not_found():
    """Когда файл не найден"""
    with patch("builtins.open", side_effect=FileNotFoundError):
        assert load_transactions("dummy.json") == []


def test_load_transactions_empty_file():
    """Обработка пустого файла"""
    with patch("builtins.open", mock_open(read_data="")):
        assert load_transactions("dummy.json") == []
