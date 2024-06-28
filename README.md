# Домашнее задание python "Виджет банковских операций клиента"
## Описание:
"Виджет банковских операций клиента" - это проект, состоящий из нескольких домашних заданий, включающий в себя поэтапную разработку функций.
Запуск проекта осуществляется через модуль `main`, расположеннsй в директории `src`

Проект состоит из четырех директорий:
  1) Директория `data` содержит файлы json, csv, xlsx
  2) Директория `logs` содержит файлы с логами
  3) Директория `src` содержит основные функции:
  - В модуле `main` реализован основной запуск проекта
  - В модуле `masks.py` реализованы две фунции с логами: 
    - `card_mask` 
    - `account_mask`
  - В модуле `widget.py` реализованы две функции: 
    - `name_card`
    - `datetime_str`
  - В модуле `processing.py` реализованы две функции:
    - `get_dict`
    - `get_sort_dict`
  - В модуле `generators.py` реализованы три функции:
    - `filter_by_currency`
    - `transaction_descriptions`
    - `card_number_generator`
  - В модуле `decorators` реализован декораторс `log`
  - В модуле `external_api` реализована функция:
    - `get_currency_rate`
  - В модуле `utils` реализованы две функции с логами:
    - `get_finance_transaction`
    - `get_transaction_amount`
  - В модуле `transactions` реализованы две функции:
    - `read_transaction_csv`
    - `read_transaction_xlsx`
  4) Директория `tests` содержит тесты, для проверки основных функций:
  - Модуль `test_masks`
  - Модуль `test_processing`
  - Модуль `test_widget`
  - Модуль `test_generators`
  - Модуль `conftest.py`
  - Модуль `test_decorators`
  - Модуль `test_external_api`
  - Модуль `test_utils`
  - Модуль `test_transactions`
