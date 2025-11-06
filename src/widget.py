"""Модуль для работы с маскировкой данных и форматированием дат."""

from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(input_string: str) -> str:
    """Маскирует номер карты или счета в строке."""

    # Разделяем строку на части (тип + номер)
    parts = input_string.strip().split()
    if len(parts) < 2:
        raise ValueError

    # Тип — элементы, кроме последнего. Номер — последний элемент
    type_part = " ".join(parts[:-1])
    number_str = parts[-1]

    # Является ли номер числом
    if not number_str.isdigit():
        raise ValueError

    number = int(number_str)

    # Если начинается с "Счет" это счет, иначе — карта
    if type_part.startswith("Счет"):
        masked_number = get_mask_account(number)
    else:
        masked_number = get_mask_card_number(number)

    return f"{type_part} {masked_number}"


"""Преобразует строку с датой из формата ISO в формат ДД.ММ.ГГГГ."""
from datetime import datetime


def get_date(date_string: str) -> str:

    dt = datetime.fromisoformat(date_string)
    # Форматируем в нужный вид
    return dt.strftime("%d.%m.%Y")
