# Цель проекта:

___Создать модуль generators, который будет содержать функции для работы с массивами транзакций.___

## Инструкция и использование:
* Функция filter_by_currency принимает список словарей на вход. 
* Функция filter_by_currency возвращает итератор. 
* Реализована функция-генератор transaction_descriptions . 
* Функция-генератор transaction_descriptions принимает на вход список словарей. 
* Функция-генератор transaction_descriptions использует yield для генерации значений по запросу. 
* Реализован генератор card_number_generator. 
* Генератор card_number_generator принимает значения start и stop в качестве аргумента.

## Примеры работы функций:

1. ___для функции filter_by_currency___
    > def filter_by_currency(transactions: List[Dict], currency_code: str) -> Iterator[Dict]:

2. ___для функции transaction_descriptions___
    > def transaction_descriptions(transactions: List[Dict]) -> Iterator[str]:

3. ___для функции card_number_generator___
    > def card_number_generator(start: int, stop: int) -> Iterator[str]:


```
*
Так же для модуля generators в папке tests/ созданы тесты с функциями. 
Функциональный код покрыт тестами более чем на 80%.
При запуске тестов командой pytest все тесты завершаются успешно.
В тестах используются фикстуры для генерации данных для теста.
В репозитории есть папка с отчетом покрытия тестами в формате HTML.
```
