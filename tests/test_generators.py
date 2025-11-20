import pytest

from src.generators import card_number_generator, filter_by_currency, transaction_descriptions


def test_filter_usd_transactions(sample_transactions):
    """Тестирование фильтрации USD транзакций"""
    usd_transactions = list(filter_by_currency(sample_transactions, "USD"))
    assert len(usd_transactions) == 3
    for transaction in usd_transactions:
        assert transaction["operationAmount"]["currency"]["code"] == "USD"


def test_filter_rub_transactions(sample_transactions):
    """Тестирование фильтрации RUB транзакций"""
    rub_transactions = list(filter_by_currency(sample_transactions, "RUB"))
    assert len(rub_transactions) == 2
    for transaction in rub_transactions:
        assert transaction["operationAmount"]["currency"]["code"] == "RUB"


def test_filter_nonexistent_currency(sample_transactions):
    """Тестирование фильтрации по несуществующей валюте"""
    eur_transactions = list(filter_by_currency(sample_transactions, "EUR"))
    assert len(eur_transactions) == 0


@pytest.mark.parametrize("currency_code,expected_count", [("USD", 3), ("RUB", 2), ("EUR", 0)])
def test_filter_with_parametrization(sample_transactions, currency_code, expected_count):
    """Тестирование фильтрации по разным валютам"""
    transactions = list(filter_by_currency(sample_transactions, currency_code))
    assert len(transactions) == expected_count


def test_descriptions_generation(sample_transactions):
    """Тестирование генерации описаний транзакций"""
    descriptions = list(transaction_descriptions(sample_transactions))
    expected_descriptions = [
        "Перевод организации",
        "Перевод со счета на счет",
        "Перевод со счета на счет",
        "Перевод с карты на карту",
        "Перевод организации",
    ]

    assert descriptions == expected_descriptions


def test_empty_transactions_list(empty_transactions):
    """Тестирование обработки пустого списка транзакций"""
    descriptions = list(transaction_descriptions(empty_transactions))
    assert len(descriptions) == 0


def test_single_transaction(sample_transactions):
    """Тестирование с одной транзакцией"""
    single_transaction = [sample_transactions[0]]
    descriptions = list(transaction_descriptions(single_transaction))
    assert len(descriptions) == 1
    assert descriptions[0] == "Перевод организации"


@pytest.mark.parametrize(
    "start,end,expected_first,expected_last,expected_count",
    [
        (1, 5, "0000 0000 0000 0001", "0000 0000 0000 0005", 5),
        (9999999999999995, 9999999999999999, "9999 9999 9999 9995", "9999 9999 9999 9999", 5),
        (1234, 1234, "0000 0000 0000 1234", "0000 0000 0000 1234", 1),
    ],
)
def test_card_number_generation(start, end, expected_first, expected_last, expected_count):
    """Параметризованное тестирование генерации номеров карт"""
    card_numbers = list(card_number_generator(start, end))
    assert len(card_numbers) == expected_count
    assert card_numbers[0] == expected_first
    assert card_numbers[-1] == expected_last


def test_card_number_format():
    """Тестирование формата номеров карт"""
    card_numbers = list(card_number_generator(1, 1))
    card_number = card_numbers[0]
    # Проверяем формат: XXXX XXXX XXXX XXXX
    assert len(card_number) == 19  # 16 цифр + 3 пробела
    assert card_number.count(" ") == 3
    # Убираем пробелы и проверяем, что остались только цифры
    digits_only = card_number.replace(" ", "")
    assert digits_only.isdigit()
    assert len(digits_only) == 16


def test_single_card_generation():
    """Тестирование генерации одной карты"""
    card_numbers = list(card_number_generator(42, 42))
    assert len(card_numbers) == 1
    assert card_numbers[0] == "0000 0000 0000 0042"


def test_large_range():
    """Тестирование генерации большого диапазона"""
    # Генерируем только первые 10 карт из большого диапазона
    generator = card_number_generator(1, 1000)
    first_ten = [next(generator) for _ in range(10)]
    assert len(first_ten) == 10
    assert first_ten[0] == "0000 0000 0000 0001"
    assert first_ten[9] == "0000 0000 0000 0010"
