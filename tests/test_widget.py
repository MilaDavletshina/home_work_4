import pytest
from src.widget import name_card, datetime_str

@pytest.mark.parametrize("number, expected", [('Maestro 1596837868705199', 'Maestro 1596 83** **** 5199'),
                                                       ('Счет 64686473678894779589', 'Счет **9589')])

def test_name_card(number, expected):
    assert name_card(number) == expected


@pytest.fixture
def date_str():
    return "11.07.2018"
def test_datetime_str(date_str):
    assert datetime_str("2018-07-11T02:26:18.671407") == date_str