from unittest.mock import patch

import pytest

from data.external_api import convert_to_rubles, get_exchange_rate


@patch.dict("os.environ", {"EXCHANGE_API_KEY": "", "EXCHANGE_API_URL": "https://api.test.com"})
def test_no_api_key():
    """Тест: отсутствует API ключ"""
    with pytest.raises(ValueError, match="API key not found"):
        get_exchange_rate("USD")


@patch.dict("os.environ", {"EXCHANGE_API_KEY": "test_key", "EXCHANGE_API_URL": ""})
def test_no_api_url():
    """Тест: отсутствует API URL"""
    with pytest.raises(ValueError, match="API URL not found"):
        get_exchange_rate("USD")


@patch("data.external_api.get_exchange_rate")
def test_convert_to_rubles_usd(mock_get_rate):
    """Тест конвертации USD в рубли"""
    mock_get_rate.return_value = 90.0

    result = convert_to_rubles(100, "USD")

    assert result == 9000.0
    mock_get_rate.assert_called_once_with("USD")


def test_convert_to_rubles_rub():
    """Тест конвертации RUB в рубли"""
    result = convert_to_rubles(1000, "RUB")
    assert result == 1000.0


def test_convert_to_rubles_unsupported_currency():
    """Тест конвертации неподдерживаемой валюты"""
    with pytest.raises(ValueError, match="Unsupported currency: GBP"):
        convert_to_rubles(100, "GBP")
