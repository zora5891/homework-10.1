import pytest

from src.widget import get_date, mask_account_card


@pytest.mark.parametrize(
    "input_str, expected",
    [
        ("Visa Platinum 7000792289606361", "Visa Platinum 7000 79** **** 6361"),
        ("Maestro 1596837868705199", "Maestro 1596 83** **** 5199"),
        ("Счет 73654108430135874305", "Счет **4305"),
        ("MasterCard 7158300734726758", "MasterCard 7158 30** **** 6758"),
    ],
)
def test_mask_account_card(input_str: str, expected: str):
    assert mask_account_card(input_str) == expected


def test_mask_account_card_invalid_number():
    with pytest.raises(ValueError, match="Номер должен состоять только из цифр"):
        mask_account_card("Visa ABC123")


def test_mask_account_card_empty_string():
    with pytest.raises(ValueError):
        mask_account_card("")


def test_mask_account_card_no_number():
    with pytest.raises(ValueError):
        mask_account_card("Visa")


def test_mask_account_card_invalid_number():
    with pytest.raises(ValueError):
        mask_account_card("Visa 123abc")


def test_get_date():
    result = get_date("2024-03-11T02:26:18.671407")
    assert result == "11.03.2024"
