import os

import requests
from dotenv import load_dotenv

load_dotenv()


def get_exchange_rate(transaction: dict) -> float:
    """Получает текущий курс конвертации в рубли на основе транзакции."""
    api_key = os.getenv("EXCHANGE_API_KEY")
    api_url = os.getenv("EXCHANGE_API_URL")

    if not api_key:
        raise ValueError("API key not found")
    if not api_url:
        raise ValueError("API URL not found")

    # Получаем валюту из транзакции
    target_currency = transaction.get("currency")
    if not target_currency:
        raise ValueError("Currency not specified in transaction")

    headers = {"apikey": api_key}
    params = {"base": "RUB", "symbols": target_currency}

    try:
        response = requests.get(api_url, headers=headers, params=params)
        response.raise_for_status()
        data = response.json()

        if "rates" in data and target_currency in data["rates"]:
            return 1 / data["rates"][target_currency]
        else:
            raise ValueError(f"Rate for {target_currency} not found in API response.")
    except requests.exceptions.RequestException as e:
        raise ConnectionError(f"Failed to fetch exchange rate: {e}")


def convert_to_rubles(transaction: dict) -> float:
    """Конвертирует сумму из указанной валюты в рубли на основе данных транзакции."""
    amount = transaction.get("amount")
    currency = transaction.get("currency")

    if amount is None:
        raise ValueError("Amount not specified in transaction")
    if currency is None:
        raise ValueError("Currency not specified in transaction")

    if currency == "RUB":
        return amount

    if currency not in ["USD", "EUR"]:
        raise ValueError(f"Unsupported currency: {currency}. Only USD, EUR, RUB are supported.")

    rate = get_exchange_rate(transaction)
    return amount * rate
