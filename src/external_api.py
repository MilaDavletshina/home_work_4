import json
import os
import requests
import external_api


from dotenv import load_dotenv

load_dotenv(".env")


API_KEY = os.getenv("API_KEY")  # ключ API


def get_currency_rate(currency: str) -> float:
    """Функция получает курс валюты с API сервера"""

    headers = {"apikey": API_KEY}  # параметр из API документации
    url = f"https://api.apilayer.com/exchangerates_data/latest?base={currency}"  # из API документации

    response = requests.get(
        url, headers=headers
    )  # отправляем запрос для получения инфо со страницы
    parsed_data = json.loads(
        response.text
    )  # преобразуем строку json в объект python (данные ввиде текста)
    currency_rate = parsed_data["rates"][
        "RUB"
    ]  # берем курс рубля по отношению к запрошенной валюте на сегодня

    return currency_rate


def get_transaction_amount(transaction) -> float:
    """Функция принимает транзакцию и возвращает сумму в рублях"""

    amount = transaction.get("amount")  # отправляем запрос для получения инфы о сумме
    currency = transaction.get(
        "currency"
    )  # отправляем запрос для получения инфы о валюте
    if currency == "RUB":
        return float(amount)
    else:
        exchange_rate = external_api.get_currency_rate(
            currency
        )  # получаем курс валюты из функции currency_rate
        if exchange_rate:
            return exchange_rate * float(amount)
        else:
            return None


print(get_transaction_amount({"amount": "2000", "currency": "USD"}))
