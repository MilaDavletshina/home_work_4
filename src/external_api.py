import json
import os
import requests


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



