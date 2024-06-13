import json
from external_api import get_currency_rate


def get_finance_transaction(input_file):
    """Функция принимает json файл и возвращает список словарей о финансовых транзакциях"""
    try:
        with open(input_file) as file:
            operations = json.load(file)
            return operations
    except:
        return []






def get_transaction_amount(transaction) -> float:
    """Функция принимает транзакцию и возвращает сумму в рублях"""

    amount = transaction.get("amount")  # отправляем запрос для получения инфы о сумме
    currency = transaction.get(
        "currency"
    )  # отправляем запрос для получения инфы о валюте
    if currency == "RUB":
        return float(amount)
    else:
        exchange_rate = get_currency_rate(
            currency
        )  # получаем курс валюты из функции currency_rate
        if exchange_rate:
            return exchange_rate * float(amount)
        else:
            return None



