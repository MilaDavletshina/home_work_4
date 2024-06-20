import pandas as pd
import pytest
import csv

from unittest.mock import patch
from src.transactions import read_transaction_csv, read_transaction_xlsx


def test_read_transaction_xlsx():
    """Тестируем чтение файла .xlsx"""
    with patch("pandas.read_excel") as mock_read_excel:
        read_transaction_xlsx("test.xlsx")
    assert mock_read_excel.called


@patch("csv.DictReader")
def test_read_transaction_csv(mock_reader):
    """Тестируем чтение файла .csv"""
    test_data = [
        {'id', 'state', 'date', 'amount', 'currency_name', 'currency_code', 'from', 'to', 'description'},
        {'650703', 'EXECUTED', '2023-09-05T11:30:32Z', '16210', 'Sol', 'PEN', 'Счет 58803664561298323391',
         'Счет 39745660563456619397', 'Перевод организации'},
        {'3598919', 'EXECUTED', '2023-09-05T11:30:32Z', '29740', 'Peso', 'PEN', 'Счет 58803664561298323391',
         'Счет 39745660563456619397', 'Перевод организации'},
    ]
    mock_reader.return_value = iter(test_data)
    result = read_transaction_csv('test.csv')
    test_data.pop(0)
    assert result == test_data
    mock_reader.assert_called_once()
