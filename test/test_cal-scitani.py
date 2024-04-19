import pytest 
from cal_scitani import *

@pytest.fixture
def calculator():
    return Calculator()

@pytest.mark.parametrize("a,b,out", [
    (1, 2, 3),
    (-1, -2, -3),
    (5, -7, -2)
])
def test_plus(a, b, out, calculator):
    assert calculator.plus(a,b) == out


@pytest.mark.parametrize("a,b,out", [
    (1, 2, -1),
    (3, 2, 1),
    (5, 7, -2)
])
def test_minus(a, b, out, calculator):
    assert calculator.minus(a,b) == out

