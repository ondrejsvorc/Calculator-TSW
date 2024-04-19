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
