import json
import logging
import os

from external_api import get_currency_rate

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(filename)s - %(levelname)s: %(message)s",
    filename="logs/utils.log",  # Запись логов в файл
    filemode="w",
)
logger = logging.getLogger()


def get_finance_transaction(input_file):
    """Функция принимает json файл и возвращает список словарей о финансовых транзакциях"""
    try:
        logger.info(f"Выполняется запрос на прием json файла: {input_file}")
        with open(input_file) as file:
            operations = json.load(file)
            logger.info("Список словарей о финансовых транзакциях загружен успешно")
            return operations
    except ValueError:
        logger.error("Список словарей не загружен - данные в файле отсутствуют")
        return []

# print(get_finance_transaction("data/operations.json"))

def get_transaction_amount(transaction) -> float:
    """Функция принимает транзакцию и возвращает сумму в рублях"""

    amount = transaction.get("amount")  # отправляем запрос для получения инфы о сумме
    currency = transaction.get(
        "currency"
    )  # отправляем запрос для получения инфы о валюте
    if currency == "RUB":
        logger.info(f'Введена валюта "RUB", конвертация не требуется')
        return float(amount)
    else:
        exchange_rate = get_currency_rate(
            currency
        )  # получаем курс валюты из функции currency_rate
        if exchange_rate:
            logger.info(f"Конвертация {currency} в RUB успешно завершена")
            return exchange_rate * float(amount)
        else:
            return None

# transaction = {"amount": "200", "currency": "USD"}
# amount = get_transaction_amount(transaction)
# print(amount)