from src.masks import get_mask_card_number, get_mask_account



if __name__ == "__main__":
    # Пример маскировки карты
    card = 7000792289606361
    masked_card = get_mask_card_number(card)
    print(f"{card} -> {masked_card}")

    # Пример маскировки счета
    account = 73654108430135874305
    masked_account = get_mask_account(account)
    print(f"{account} -> {masked_account}")
