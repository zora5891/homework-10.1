import os
from typing import Dict

import requests
from dotenv import load_dotenv

load_dotenv()

EXCHANGE_API_URL = "https://api.exchangerate-api.com/v4/latest/USD"
API_KEY = os.getenv("EXCHANGE_API_KEY")


def get_exchange_rate(currency: str) -> float:
    """Получает текущий курс валюты"""
    try:
        response = requests.get(f"{EXCHANGE_API_URL}?access_key={API_KEY}")
        response.raise_for_status()
        data = response.json()
        return data["rates"].get(currency, 1.0)
    except requests.RequestException:
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
    return amount
