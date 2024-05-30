from src.generators import (
    card_number_generator,
    filter_by_currency,
    transaction_descriptions,
)
import pytest


def test_filter_by_currency_usd(operations):
    usd_currency = filter_by_currency(operations, "USD")
    assert next(usd_currency)["id"] == 939719570
    assert next(usd_currency)["id"] == 142264268
    assert next(usd_currency)["id"] == 895315941


def test_filter_by_currency_rub(operations):
    rub_currency = filter_by_currency(operations, "RUB")
    assert next(rub_currency)["id"] == 873106923
    assert next(rub_currency)["id"] == 594226727


def test_transaction_descriptions(operations):
    description = transaction_descriptions(operations)
    assert next(description) == "Перевод организации"
    assert next(description) == "Перевод со счета на счет"
    assert next(description) == "Перевод со счета на счет"
    assert next(description) == "Перевод с карты на карту"
    assert next(description) == "Перевод организации"


@pytest.mark.parametrize(
    "start, end, expected",
    [
        (1, 1, "0000 0000 0000 0001"),
        (2, 2, "0000 0000 0000 0002"),
        (3, 3, "0000 0000 0000 0003"),
        (4, 4, "0000 0000 0000 0004"),
        (5, 5, "0000 0000 0000 0005"),
    ],
)
def test_card_number_generator(start, end, expected):
    card_number = card_number_generator(start, end)
    assert next(card_number) == expected
