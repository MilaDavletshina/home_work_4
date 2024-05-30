import pytest
from src.decorators import log, my_function


@pytest.mark.parametrize("x, y, expected", [(1, 2, 3), (5, 5, 10)])
def test_my_function(capsys, x, y, expected):
    my_function(x, y)
    addition = capsys.readouterr()
    assert addition.out == f"{expected}\n"


def test_log():
    with pytest.raises(ValueError, match="my_function: ValueError. Inputs (1,), {}"):
        my_function(1, 2)
