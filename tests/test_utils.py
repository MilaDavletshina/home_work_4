import pytest
import json

from src.utils import get_finance_transaction


def test_get_finance_transaction():
    input_file = "test.json"

    data = [{"id": 895315941, "amount": 56883.54}]

    with open(input_file, "w") as file:
        json.dump(data, file)
    assert get_finance_transaction(input_file) == [
        {"id": 895315941, "amount": 56883.54}
    ]


def test_get_finance_transaction_empty_input():
    input_file = "test_empty_file.json"
    with open(input_file, "w") as file:
        file.write("")
        assert get_finance_transaction(input_file) == []


def test_get_finance_transaction_invalid_input():
    input_file = "test_invalid_file.json"
    with open(input_file, "w") as file:
        file.write('{"id": 1, "amount": 100,}')
        assert get_finance_transaction(input_file) == []
