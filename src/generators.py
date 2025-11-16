from typing import Dict, Iterator, List


def filter_by_currency(transactions: List[Dict], currency_code: str) -> Iterator[Dict]:
    """Фильтрует транзакции по заданной валюте."""
    for transaction in transactions:
        operation_amount = transaction.get("operationAmount", {})
        currency = operation_amount.get("currency", {})
        if currency.get("code") == currency_code:
            yield transaction


def transaction_descriptions(transactions: List[Dict]) -> Iterator[str]:
    """Генерирует описания транзакций."""
    for transaction in transactions:
        yield transaction["description"]


def card_number_generator(start: int, stop: int) -> Iterator[str]:
    """Генерирует номера банковских карт в заданном диапазоне."""
    for number in range(start, stop + 1):
        # Форматируем номер как 16-значную строку с ведущими нулями
        card_number_str = str(number).zfill(16)
        # Разбиваем на группы по 4 цифры
        formatted_number = " ".join([card_number_str[i : i + 4] for i in range(0, 16, 4)])
        yield formatted_number
