from typing import Any, Dict, List

import pytest


@pytest.fixture
def mask_input_strings() -> List[str]:
    """Фикстура: строки для тестирования mask_account_card."""
    return [
        "Visa Platinum 7000792289606361",
        "Maestro 1596837868705199",
        "MasterCard 7158300734726758",
        "Visa Classic 6831982476737658",
        "Счет 73654108430135874305",
        "Счет 64686473678894779589",
    ]


@pytest.fixture
def date_strings() -> List[str]:
    """Фикстура: валидные строки дат в формате ISO."""
    return [
        "2 prepared",
        "2024-03-11T02:26:18.671407",
        "2023-12-25T10:15:30.123456",
        "2022-01-01T00:00:00.000000",
    ]


@pytest.fixture
def invalid_numbers() -> List[int]:
    """Фикстура: некорректные номера (не 16 для карт, не число и т.п.)."""
    return [12345, 123456789012345, 123]


@pytest.fixture
def card_numbers() -> List[int]:
    """Фикстура: список номеров карт (16 цифр)."""
    return [
        7000792289606361,
        1596837868705199,
        7158300734726758,
        6831982476737658,
        8990922113665229,
        5999414228426353,
    ]


@pytest.fixture
def sample_data() -> List[Dict[str, Any]]:
    """Фикстура: список словарей для тестов фильтрации и сортировки."""
    return [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
    ]
