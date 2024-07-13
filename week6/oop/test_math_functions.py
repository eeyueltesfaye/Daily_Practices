# test_math_functions.py

from math_functions import add, subtract

def test_add():
    assert add(1, 2) == 3
    assert add(-1, 1) == 0
    assert add(-1, -1) == -2

def test_subtract():
    assert subtract(2, 1) == 1
    assert subtract(2, 2) == 0
    assert subtract(2, 3) == -1
