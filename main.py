from src.masks import get_mask_account, get_mask_card_number
from src.widget import get_date, mask_account_card
from src.generators import filter_by_currency, transaction_descriptions, card_number_generator

transactions = [
    {
        "id": 939719570,
        "state": "EXECUTED",
        "date": "2018-06-30T02:08:58.425572",
        "operationAmount": {
            "amount": "9824.07",
            "currency": {"name": "USD", "code": "USD"},
        },
        "description": "Перевод организации",
        "from": "Счет 75106830613657916952",
        "to": "Счет 11776614605963066702",
    },
    {
        "id": 142264268,
        "state": "EXECUTED",
        "date": "2019-04-04T23:20:05.206878",
        "operationAmount": {
            "amount": "79114.93",
            "currency": {"name": "USD", "code": "USD"},
        },
        "description": "Перевод со счета на счет",
        "from": "Счет 19708645243227258542",
        "to": "Счет 75651667383060284188",
    },
]

if __name__ == "__main__":
    # Пример маскировки карты
    card = 7000792289606361
    masked_card = get_mask_card_number(card)
    print(f"{card} -> {masked_card}")

    # Пример маскировки счета
    account = 73654108430135874305
    masked_account = get_mask_account(account)
    print(f"{account} -> {masked_account}")

    # Примеры маскировки данных и форматирование даты
    print(mask_account_card("Maestro 1596837868705199"))
    print(mask_account_card("Счет 64686473678894779589"))
    print(get_date("2024-03-11T02:26:18.671407"))

    # Пример использования filter_by_currency
    usd_transactions = filter_by_currency(transactions, "USD")
    for transaction in usd_transactions:
        print(f"  - {transaction['description']}: {transaction['operationAmount']['amount']} USD")

    # Пример использования transaction_descriptions
    descriptions = transaction_descriptions(transactions)
    for description in descriptions:
        print(f"  - {description}")

    # Пример использования card_number_generator
    for card_number in card_number_generator(1, 5):
        print(f"  - {card_number}")
