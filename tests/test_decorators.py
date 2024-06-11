import pytest
from src.decorators import my_function, log


@pytest.mark.parametrize("x, y, expected", [(1, 2, 3), (5, 5, 10)])
def test_my_function(capsys, x, y, expected):
    my_function(x, y)
    addition = capsys.readouterr()
    assert addition.out == f"{expected}\n"
