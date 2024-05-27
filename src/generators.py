
def filter_by_currency(transactions, currency):
    """Функция принимает список словарей с банковскими операциями и возвращает итератор, который выдает по очереди операции, в которых указана заданная валюта"""
    with open("transactions.txt") as file:
    for transaction in transactions:
        if transaction['operationAmount']['currency']['code'] == currency:
            yield transaction
