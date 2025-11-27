import os
from typing import Dict

import requests
from dotenv import load_dotenv

load_dotenv()

EXCHANGE_API_URL = "https://marketplace.apilayer.com/exchangerates_data-api"
API_KEY = os.getenv("EXCHANGE_API_KEY")


def get_exchange_rate(currency: str) -> float:
    """Получает текущий курс валюты"""
    try:
        url = f"{EXCHANGE_API_URL}?access_key={API_KEY}"
        print(f"Отправляем запрос: {url}")

        response = requests.get(f"{EXCHANGE_API_URL}?access_key={API_KEY}")
        response.raise_for_status()
        data = response.json()
        if not data.get("success", False):
            error_msg = data.get("error", "Unknown error")
            raise ValueError(f"API error: {error_msg}")

        rate = data["rates"].get(currency)
        if rate is None:
            print(f"Курс для {currency} не найден, используем 1.0")
        return 1.0

    except (requests.RequestException, ValueError, KeyError, TypeError) as e:
        print(f"Ошибка при получении курса {currency}: {e}")
    return 1.0


def convert_amount_to_rub(transaction: Dict) -> float:
    """Конвертирует сумму транзакции в рубли"""
    amount = float(transaction["operationAmount"]["amount"])
    currency = transaction["operationAmount"]["currency"]["code"]

    if currency == "RUB":
        return amount
    elif currency in ["USD", "EUR"]:
        rate = get_exchange_rate(currency)
        return amount * rate
    else:
        print(f"Неподдерживаемая валюта: {currency}, используем курс 1.0")
        return amount