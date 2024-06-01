from itertools import count


def filter_by_currency(transactions, currency):
    """Функция принимает список словарей с банковскими операциями и возвращает итератор, который выдает по очереди операции, в которых указана заданная валюта"""
    for transaction in transactions:
        if transaction["operationAmount"]["currency"]["code"] == currency:
            yield transaction


def transaction_descriptions(transactions):
    """Функция принимает список словарей и возвращает описание каждой операции по очереди"""
    for transaction in transactions:
        yield transaction["description"]


def card_number_generator(start: int, end: int) -> str:
    """Функция генерирует номера карт в формате XXXX XXXX XXXX XXXX"""
    for i in count(start):
        if i > end:
            break
        yield "{:04d} {:04d} {:04d} {:04d}".format(
            (i // 1000) % 10, (i // 100) % 10, (i // 10) % 10, i % 10
        )
