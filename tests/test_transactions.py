import pandas as pd
import pytest
import csv

from unittest.mock import patch
from src.transactions import read_transaction_csv, read_transaction_xlsx


def test_read_transaction_xlsx():
    with patch("pandas.read_excel") as mock_read_excel:
        read_transaction_xlsx("test.xlsx")
    assert mock_read_excel.called


@patch("csv.reader")
def test_read_transaction_csv(mock_reader):
    mock_reader.return_value = iter(
        [
            [
                "id",
                "state",
                "date",
                "amount",
                "currency_name",
                "currency_code",
                "from",
                "to",
                "description",
            ],
            [
                "650703",
                "EXECUTED",
                "2023-09-05T11:30:32Z",
                "16210",
                "SoL",
                "PEN",
                "Счет 58803664651298323391",
                "Счет 39746506635466619397",
                "Перевод организации",
            ],
        ]
    )
    assert read_transaction_csv("data/transactions.csv") == [
        [
            "id",
            "state",
            "date",
            "amount",
            "currency_name",
            "currency_code",
            "from",
            "to",
            "description",
        ],
        [
            "650703",
            "EXECUTED",
            "2023-09-05T11:30:32Z",
            "16210",
            "SoL",
            "PEN",
            "Счет 58803664651298323391",
            "Счет 39746506635466619397",
            "Перевод организации",
        ],
    ]
    mock_reader.assert_called_once()
