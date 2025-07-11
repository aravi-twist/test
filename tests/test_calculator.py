import pytest
from calculator_project.calculator import (
    add, subtract, multiply, divide, power, modulus, sqrt, factorial,
    average, maximum, minimum, product
)

def test_add():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0
    assert add(0, 0) == 0
    assert add(1.5, 2.5) == 4.0

def test_subtract():
    assert subtract(5, 2) == 3
    assert subtract(0, 4) == -4
    assert subtract(-3, -3) == 0
    assert subtract(2.5, 1.5) == 1.0

def test_multiply():
    assert multiply(3, 4) == 12
    assert multiply(-2, 5) == -10
    assert multiply(0, 100) == 0
    assert multiply(2.5, 2) == 5.0

@pytest.mark.parametrize("a,b,expected", [
    (10, 2, 5),
    (3, 1.5, 2),
    (-6, -2, 3),
    (0, 1, 0),
])
def test_divide(a, b, expected):
    assert divide(a, b) == expected

def test_divide_zero():
    with pytest.raises(ValueError):
        divide(5, 0)

def test_power():
    assert power(2, 3) == 8
    assert power(5, 0) == 1
    assert power(2, -2) == 0.25
    assert power(-2, 3) == -8

def test_modulus():
    assert modulus(10, 3) == 1
    assert modulus(9, 3) == 0
    assert modulus(-7, 4) == 1
    with pytest.raises(ValueError):
        modulus(5, 0)

def test_sqrt():
    assert sqrt(4) == 2
    assert sqrt(0) == 0
    assert sqrt(2.25) == 1.5
    with pytest.raises(ValueError):
        sqrt(-1)

def test_factorial():
    assert factorial(0) == 1
    assert factorial(5) == 120
    with pytest.raises(ValueError):
        factorial(-1)
    with pytest.raises(ValueError):
        factorial(2.5)

def test_average():
    assert average(2, 4, 6) == 4
    assert average(5) == 5
    assert average(1.5, 2.5) == 2.0
    with pytest.raises(ValueError):
        average()

def test_maximum():
    assert maximum(1, 2, 3) == 3
    assert maximum(-1, -2, -3) == -1
    assert maximum(5) == 5
    with pytest.raises(ValueError):
        maximum()

def test_minimum():
    assert minimum(1, 2, 3) == 1
    assert minimum(-1, -2, -3) == -3
    assert minimum(5) == 5
    with pytest.raises(ValueError):
        minimum()

def test_product():
    assert product(2, 3, 4) == 24
    assert product(5) == 5
    assert product(1.5, 2) == 3.0
    with pytest.raises(ValueError):
        product()
