import os

import requests
from dotenv import load_dotenv

load_dotenv()


def get_exchange_rate(target_currency: str) -> float:
    """Получает текущий курс конвертации в рубли"""
    api_key = os.getenv("EXCHANGE_API_KEY")
    api_url = os.getenv("EXCHANGE_API_URL")

    if not api_key:
        raise ValueError("API key not found")
    if not api_url:
        raise ValueError("API URL not found")

    headers = {"apikey": api_key}
    params = {"base": "RUB", "symbols": target_currency}

    try:
        response = requests.get(api_url, headers=headers, params=params)
        response.raise_for_status()
        data = response.json()

        if "rates" in data and target_currency in data["rates"]:
            # API возвращает курс как 1 RUB = X USD/EUR
            return 1 / data["rates"][target_currency]
        else:
            raise ValueError(f"Rate for {target_currency} not found in API response.")
    except requests.exceptions.RequestException as e:
        raise ConnectionError(f"Failed to fetch exchange rate: {e}")


def convert_to_rubles(amount: float, currency: str) -> float:
    """Конвертирует сумму из указанной валюты в рубли."""
    if currency == "RUB":
        return amount

    if currency not in ["USD", "EUR"]:
        raise ValueError(f"Unsupported currency: {currency}. Only USD, EUR, RUB are supported.")

    rate = get_exchange_rate(currency)
    return amount * rate
