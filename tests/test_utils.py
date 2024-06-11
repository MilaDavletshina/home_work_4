import pytest
from src.utils import get_finance_transaction


def test_get_finance_transaction_empty_input():
    input_file = 'test_empty_file.json'
    with open(input_file, 'w') as file:
        file.write('')
        assert get_finance_transaction(input_file) == []

def test_get_finance_transaction_invalid_input():
    input_file = 'test_invalid_file.json'
    with open(input_file, 'w') as file:
        file.write('{"id": 1, "amount": 100,}')
        assert get_finance_transaction(input_file) == []