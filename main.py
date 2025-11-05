from src.masks import get_mask_card_number, get_mask_account
from src.widget import mask_account_card, get_date


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
