from src.generators import filter_by_currency, transaction_descriptions, card_number_generator
import pytest

def test_filter_by_currency_usd(transactions, currency):
    currency_usd = filter_by_currency(transactions, "USD")
    assert next (currency_usd)['id'] == 939719570
    assert next(currency_usd)['id'] == 142264268
    assert next(currency_usd)['id'] == 895315941

def test_filter_by_currency_rub(transactions, currency):
    currency_rub = filter_by_currency(transactions, "RUB")
    assert next (currency_rub)['id'] == 873106923
    assert next(currency_rub)['id'] == 594226727


def test_transaction_descriptions(transactions):
    description = transaction_descriptions(transactions)
    assert next(description) == 'Перевод организации'
    assert next(description) == 'Перевод со счета на счет'
    assert next(description) == 'Перевод со счета на счет'
    assert next(description) == 'Перевод с карты на карту'
    assert next(description) == 'Перевод организации'


@pytest.mark.parametrize('start, end, expected', [(0000 0000 0000 0001, 0000 0000 0000 0001, 0000 0000 0000 0001),
                                                  (0000 0000 0000 0002, 0000 0000 0000 0002, 0000 0000 0000 0002),
                                                  (0000 0000 0000 0005, 0000 0000 0000 0005, 0000 0000 0000 0005),],)

def test_card_number_generator(start, end, expected):
    assert card_number_generator(start, end) == expected

