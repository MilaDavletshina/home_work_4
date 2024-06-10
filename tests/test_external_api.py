import os

from unittest.mock import patch
from dotenv import load_dotenv

from src.external_api import get_currency_rate


load_dotenv(".env")
API_KEY = os.getenv("API_KEY")
headers = {"apikey": API_KEY}



@patch("request.get")
def test_get_currency_rate(mock_get):
    mock_get.return_value.json.return_value = {
        "base": "EUR",
        "date": "2024-06-10",
        "rates": {"RUB": 95.719978},
        "success": true,
        "timestamp": 1718001729
    }

    assert get_currency_rate("EUR") == 95.719978
    mock_get.assert_called_once_with('https://api.apilayer.com/exchangerates_data/latest?base=EUR')


