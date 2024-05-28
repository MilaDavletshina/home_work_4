from src.generators import (card_number_generator, filter_by_currency,
                            transaction_descriptions)


def test_filter_by_currency_usd(transactions, currency):
    currency_usd = filter_by_currency(transactions, "USD")
    assert next(currency_usd)["id"] == 939719570
    assert next(currency_usd)["id"] == 142264268
    assert next(currency_usd)["id"] == 895315941


def test_filter_by_currency_rub(transactions, currency):
    currency_rub = filter_by_currency(transactions, "RUB")
    assert next(currency_rub)["id"] == 873106923
    assert next(currency_rub)["id"] == 594226727


def test_transaction_descriptions(transactions):
    description = transaction_descriptions(transactions)
    assert next(description) == "Перевод организации"
    assert next(description) == "Перевод со счета на счет"
    assert next(description) == "Перевод со счета на счет"
    assert next(description) == "Перевод с карты на карту"
    assert next(description) == "Перевод организации"


def test_card_number_generator(start, end):
    card_number = card_number_generator(1, 5)
    assert next(card_number) == "0000 0000 0000 0001"
    assert next(card_number) == "0000 0000 0000 0002"
    assert next(card_number) == "0000 0000 0000 0003"
    assert next(card_number) == "0000 0000 0000 0004"
    assert next(card_number) == "0000 0000 0000 0005"
