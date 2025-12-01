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


@patch("requests.get")
def test_convert_to_rubles_rub(mock_get):
    """Если валюта уже в RUB — API не вызывается."""
    transaction = {"amount": 150.0, "currency": "RUB"}
    result = convert_to_rubles(transaction)

    assert result == 150.0
    mock_get.assert_not_called()  # API не должен быть вызван


@patch("requests.get")
def test_convert_to_rubles_api_error(mock_get):
    """Если API вернуло ошибку (например, 404)"""
    mock_get.return_value.raise_for_status.side_effect = Exception("API key not found")

    transaction = {"amount": 100.0, "currency": "USD"}

    with pytest.raises(Exception, match="API key not found"):
        convert_to_rubles(transaction)
