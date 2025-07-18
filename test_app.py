from math_app import add, subtract, multiply, divide, exponent, modulo
import pytest

def test_add():
    assert add(2, 3) == 5

def test_subtract():
    assert subtract(10, 4) == 6

def test_multiply():
    assert multiply(3, 5) == 15 

def test_divide():
    assert divide(9, 3) == 3

def test_divide_by_zero():
    with pytest.raises(ValueError):
        divide(5, 0)

def test_exponent():
    assert exponent(2, 3) == 8

def test_modulo():
    assert modulo(10, 3) == 1
