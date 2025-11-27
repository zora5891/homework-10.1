from unittest.mock import patch

import pytest
import requests

from data.external_api import convert_amount_to_rub, get_exchange_rate


@pytest.mark.parametrize(
    "transaction,expected",
    [
        ({"operationAmount": {"amount": "100", "currency": {"name": "USD", "code": "USD"}}}, 100),
        ({"operationAmount": {"amount": "100", "currency": {"name": "EUR", "code": "EUR"}}}, 100),
        ({"operationAmount": {"amount": "100", "currency": {"name": "RUB", "code": "RUB"}}}, 100),
    ],
)
def test_convert_amount_to_rub(transaction, expected):
    """Конвертация суммы транзакции в рубли"""
    with patch("data.external_api.get_exchange_rate", return_value=1.0):
        assert convert_amount_to_rub(transaction) == float(expected)


def test_get_exchange_rate():
    """Получение курса валют"""
    with patch("requests.get") as mock_get:
        mock_get.return_value.json.return_value = {"rates": {"USD": 1.0, "EUR": 1.0}}


def test_get_exchange_rate_error():
    """Обработка ошибок при получении курса валют"""
    with patch("requests.get") as mock_get:
        mock_get.side_effect = requests.RequestException
        rate = get_exchange_rate("USD")
        assert rate == 1.0


def test_convert_amount_invalid_currency():
    """Оработка неподдерживаемой валюты"""
    transaction = {"operationAmount": {"amount": "100", "currency": {"name": "GBP", "code": "GBP"}}}
    with patch("data.external_api.get_exchange_rate") as mock_rate:
        # Проверяем, что метод не вызывается для неподдерживаемой валюты
        mock_rate.assert_not_called()

        # Проверяем результат конвертации
        result = convert_amount_to_rub(transaction)
        assert result == 100.0  # Возвращаем исходную сумму
        assert isinstance(result, float)  # Проверяем тип данных
