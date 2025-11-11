import pytest

from src.masks import get_mask_card_number


@pytest.mark.parametrize('card_num, expected', [
    (7000792289606361, '7000 79** **** 6361'),
    (1596837868705199, '1596 83** **** 5199'),
    (7158300734726758, '7158 30** **** 6758'),
])
def test_get_mask_card_number(card_num: int, expected: str):
    assert get_mask_card_number(card_num) == expected


def test_get_mask_card_number_invalid_length(invalid_numbers):
    for num in invalid_numbers:
        with pytest.raises(ValueError, match="Номер карты должен содержать 16 цифр"):
            get_mask_card_number(num)
