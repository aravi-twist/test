import pytest
import math
from calculator_project.calculator import (
    add, subtract, multiply, divide, power, modulus, sqrt, factorial,
    average, maximum, minimum, product, abs_val, reciprocal, log, exp, round_number,
    # Trigonometric functions
    sin, cos, tan, asin, acos, atan, atan2, sinh, cosh, tanh,
    degrees_to_radians, radians_to_degrees,
    # Foreign exchange functions
    get_exchange_rates, convert_currency, get_currency_list, calculate_currency_spread,
    # Financial functions
    calculate_compound_interest, calculate_simple_interest, calculate_loan_payment,
    # Advanced math functions
    gcd, lcm, is_prime, fibonacci, binomial_coefficient
)

# Basic arithmetic tests
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

# Additional basic function tests
def test_abs_val():
    assert abs_val(-5) == 5
    assert abs_val(5) == 5
    assert abs_val(0) == 0
    assert abs_val(-3.14) == 3.14

def test_reciprocal():
    assert reciprocal(2) == 0.5
    assert reciprocal(0.25) == 4.0
    assert reciprocal(-2) == -0.5
    with pytest.raises(ValueError):
        reciprocal(0)

def test_log():
    assert log(math.e) == 1.0
    assert log(1) == 0.0
    assert log(100, 10) == 2.0
    with pytest.raises(ValueError):
        log(0)
    with pytest.raises(ValueError):
        log(-1)

def test_exp():
    assert exp(0) == 1.0
    assert exp(1) == math.e
    assert exp(-1) == 1/math.e

def test_round_number():
    assert round_number(3.14159, 2) == 3.14
    assert round_number(3.14159) == 3
    assert round_number(-3.7) == -4

# Trigonometric function tests
def test_sin():
    assert sin(0, degrees=True) == 0.0
    assert abs(sin(30, degrees=True) - 0.5) < 1e-10
    assert abs(sin(90, degrees=True) - 1.0) < 1e-10
    assert abs(sin(math.pi/2) - 1.0) < 1e-10  # radians

def test_cos():
    assert cos(0, degrees=True) == 1.0
    assert abs(cos(60, degrees=True) - 0.5) < 1e-10
    assert abs(cos(90, degrees=True)) < 1e-10
    assert abs(cos(math.pi/2)) < 1e-10  # radians

def test_tan():
    assert tan(0, degrees=True) == 0.0
    assert abs(tan(45, degrees=True) - 1.0) < 1e-10
    assert abs(tan(math.pi/4) - 1.0) < 1e-10  # radians

def test_asin():
    assert asin(0) == 0.0
    assert abs(asin(0.5) - math.pi/6) < 1e-10
    assert abs(asin(1) - math.pi/2) < 1e-10
    with pytest.raises(ValueError):
        asin(2)
    with pytest.raises(ValueError):
        asin(-2)

def test_acos():
    assert acos(1) == 0.0
    assert abs(acos(0.5) - math.pi/3) < 1e-10
    assert abs(acos(0) - math.pi/2) < 1e-10
    with pytest.raises(ValueError):
        acos(2)
    with pytest.raises(ValueError):
        acos(-2)

def test_atan():
    assert atan(0) == 0.0
    assert abs(atan(1) - math.pi/4) < 1e-10
    assert abs(atan(-1) + math.pi/4) < 1e-10

def test_atan2():
    assert atan2(0, 1) == 0.0
    assert abs(atan2(1, 1) - math.pi/4) < 1e-10
    assert abs(atan2(1, 0) - math.pi/2) < 1e-10
    assert abs(atan2(-1, 0) + math.pi/2) < 1e-10

def test_sinh():
    assert sinh(0) == 0.0
    assert abs(sinh(1) - 1.175201194) < 1e-9
    assert abs(sinh(-1) + 1.175201194) < 1e-9

def test_cosh():
    assert cosh(0) == 1.0
    assert abs(cosh(1) - 1.543080635) < 1e-9
    assert cosh(-1) == cosh(1)

def test_tanh():
    assert tanh(0) == 0.0
    assert abs(tanh(1) - 0.761594156) < 1e-9
    assert tanh(-1) == -tanh(1)

def test_degrees_to_radians():
    assert degrees_to_radians(0) == 0.0
    assert degrees_to_radians(180) == math.pi
    assert degrees_to_radians(360) == 2 * math.pi

def test_radians_to_degrees():
    assert radians_to_degrees(0) == 0.0
    assert radians_to_degrees(math.pi) == 180.0
    assert radians_to_degrees(2 * math.pi) == 360.0

# Foreign exchange tests
def test_get_exchange_rates():
    rates = get_exchange_rates()
    assert isinstance(rates, dict)
    assert 'USD' in rates
    assert 'EUR' in rates
    assert 'GBP' in rates
    assert rates['USD'] == 1.0

def test_convert_currency():
    # Test USD to EUR conversion
    result = convert_currency(100, 'USD', 'EUR')
    assert result == 85.0
    
    # Test EUR to USD conversion
    result = convert_currency(85, 'EUR', 'USD')
    assert result == 100.0
    
    # Test USD to USD (should be same)
    result = convert_currency(100, 'USD', 'USD')
    assert result == 100.0
    
    # Test case insensitivity
    result = convert_currency(100, 'usd', 'eur')
    assert result == 85.0

def test_convert_currency_invalid():
    with pytest.raises(ValueError):
        convert_currency(100, 'USD', 'XYZ')
    with pytest.raises(ValueError):
        convert_currency(100, 'XYZ', 'USD')

def test_get_currency_list():
    currencies = get_currency_list()
    assert isinstance(currencies, list)
    assert 'USD' in currencies
    assert 'EUR' in currencies
    assert 'GBP' in currencies
    assert len(currencies) >= 20

def test_calculate_currency_spread():
    spread = calculate_currency_spread(1.20, 1.25)
    assert abs(spread - 4.166666667) < 1e-9
    
    spread = calculate_currency_spread(1.0, 1.0)
    assert spread == 0.0
    
    with pytest.raises(ValueError):
        calculate_currency_spread(0, 1.25)
    with pytest.raises(ValueError):
        calculate_currency_spread(1.20, 0)
    with pytest.raises(ValueError):
        calculate_currency_spread(-1, 1.25)

# Financial calculation tests
def test_calculate_compound_interest():
    # Simple case: $1000 at 5% for 1 year, annual compounding
    result = calculate_compound_interest(1000, 0.05, 1)
    assert result == 1050.0
    
    # Monthly compounding
    result = calculate_compound_interest(1000, 0.05, 1, 12)
    assert abs(result - 1051.16) < 0.01
    
    # Zero interest rate
    result = calculate_compound_interest(1000, 0, 5)
    assert result == 1000.0

def test_calculate_simple_interest():
    result = calculate_simple_interest(1000, 0.05, 1)
    assert result == 50.0
    
    result = calculate_simple_interest(1000, 0.05, 5)
    assert result == 250.0
    
    result = calculate_simple_interest(1000, 0, 5)
    assert result == 0.0

def test_calculate_loan_payment():
    # Test with 0% interest (simple division)
    payment = calculate_loan_payment(12000, 0, 1, 12)
    assert payment == 1000.0
    
    # Test with interest (monthly payment for $200k at 4% for 30 years)
    payment = calculate_loan_payment(200000, 0.04, 30, 12)
    assert abs(payment - 954.83) < 0.01

# Advanced math function tests
def test_gcd():
    assert gcd(48, 18) == 6
    assert gcd(0, 5) == 5
    assert gcd(5, 0) == 5
    assert gcd(0, 0) == 0
    assert gcd(17, 13) == 1  # Coprime numbers

def test_lcm():
    assert lcm(12, 18) == 36
    assert lcm(0, 5) == 0
    assert lcm(5, 0) == 0
    assert lcm(17, 13) == 221  # Coprime numbers

def test_is_prime():
    assert is_prime(2) == True
    assert is_prime(3) == True
    assert is_prime(4) == False
    assert is_prime(17) == True
    assert is_prime(25) == False
    assert is_prime(29) == True
    assert is_prime(1) == False
    assert is_prime(0) == False
    assert is_prime(-1) == False

def test_fibonacci():
    assert fibonacci(0) == 0
    assert fibonacci(1) == 1
    assert fibonacci(2) == 1
    assert fibonacci(3) == 2
    assert fibonacci(4) == 3
    assert fibonacci(5) == 5
    assert fibonacci(6) == 8
    assert fibonacci(10) == 55
    
    with pytest.raises(ValueError):
        fibonacci(-1)

def test_binomial_coefficient():
    assert binomial_coefficient(5, 2) == 10
    assert binomial_coefficient(5, 0) == 1
    assert binomial_coefficient(5, 5) == 1
    assert binomial_coefficient(0, 0) == 1
    assert binomial_coefficient(5, 6) == 0  # k > n
    assert binomial_coefficient(5, -1) == 0  # k < 0

# Edge cases and error handling tests
def test_edge_cases():
    # Test very large numbers
    assert add(1e10, 1e10) == 2e10
    
    # Test very small numbers
    assert add(1e-10, 1e-10) == 2e-10
    
    # Test trigonometric edge cases
    assert abs(sin(180, degrees=True)) < 1e-10
    assert abs(cos(180, degrees=True) + 1) < 1e-10

def test_type_validation():
    # Test that factorial only accepts integers
    with pytest.raises(ValueError):
        factorial(3.5)
    
    # Note: Python's built-in math.gcd and our implementation accept floats
    # but convert them to integers, so we don't test for TypeError here

# Integration tests
def test_trigonometric_identities():
    # Test that sin² + cos² = 1
    angle = 45
    sin_val = sin(angle, degrees=True)
    cos_val = cos(angle, degrees=True)
    assert abs(sin_val**2 + cos_val**2 - 1) < 1e-10
    
    # Test that tan = sin/cos
    tan_val = tan(angle, degrees=True)
    assert abs(tan_val - sin_val/cos_val) < 1e-10

def test_currency_conversion_consistency():
    # Test that converting back and forth gives the original amount
    original_amount = 100
    from_curr = 'USD'
    to_curr = 'EUR'
    
    converted = convert_currency(original_amount, from_curr, to_curr)
    converted_back = convert_currency(converted, to_curr, from_curr)
    
    assert abs(converted_back - original_amount) < 1e-10

def test_financial_calculations_consistency():
    # Test that simple interest is less than compound interest for same parameters
    principal = 1000
    rate = 0.05
    time = 5
    
    simple = calculate_simple_interest(principal, rate, time)
    compound = calculate_compound_interest(principal, rate, time) - principal
    
    assert simple < compound
