# Цель проекта:

__Написать тесты ко всем функциям проекта__

## Инструкция и использование:
```
Тесты находятся в новой ветки домашней работы feature/homework_10_2
```
* Модули тестируются в отдельных тестовых файлах. 
* Функциональный код покрыт тестами более чем на 80%. 
* При запуске тестов командой pytest все тесты завершаются успешно.

## Примеры работы функций:
```
Для каждого модуля в папке src/ созданы тесты с функциями:
```

1. ___для модуля masks.py___
    > tests/test_masks.py
- def test_get_mask_card_number
- def test_get_mask_card_number_invalid_length

2. ___для модуля widget.py___
    > tests/test_widget.py
- def test_mask_account_card
- def test_mask_account_card_invalid_number
- def test_mask_account_card_no_number
- def test_mask_account_card_empty_string
- def test_get_date

3. ___для модуля test_processing.py___
    > tests/test_processing.py
- def test_filter_by_state_default
- def test_filter_by_state_canceled
- def test_sort_by_date_descending

***Так же в проекте применины фикстуры для создания необходимых входных данных для тестов,
и использованна параметризация в тестах для обеспечения тестирования функциональности с различными входными данными.***