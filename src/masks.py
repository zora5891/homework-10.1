"""Модуль для маскировки номеров банковских карт и счетов."""


def get_mask_card_number(card_number: int) -> str:
    """
    Args:
        card_number: Номер карты в виде целого числа.
    Returns:
        Строка с маской номера карты в формате 'XXXX XX** **** XXXX'.
    Example:
        >>> get_mask_card_number(7000792289606361)
        '7000 79** **** 6361'
    """
    card_str = str(card_number)
    if len(card_str) != 16:
        raise ValueError("Номер карты должен содержать 16 цифр")

    first_part = card_str[:4]
    second_part = card_str[4:6]

    last_part = card_str[-4:]

    masked = f"{first_part} {second_part}** **** {last_part}"
    return masked


def get_mask_account(account_number: int) -> str:
    """
    Args:
        account_number: Номер счета в виде целого числа.
    Returns:
        Строка с маской номера счета в формате '**XXXX'.
    Example:
        >>> get_mask_account(73654108430135874305)
        '**4305'
    """
    account_str = str(account_number)

    last_four = account_str[-4:]

    masked = f"**{last_four}"
    return masked
