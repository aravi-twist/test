"""
A more advanced calculator module providing basic and advanced arithmetic operations,
trigonometric functions, and foreign exchange calculations.
"""

import math
import operator
from functools import reduce
import requests
from typing import Dict, Optional, Union

# Foreign exchange rates (as of a recent date - in production, you'd want to fetch live rates)
DEFAULT_EXCHANGE_RATES = {
    'USD': 1.0,
    'EUR': 0.85,
    'GBP': 0.73,
    'JPY': 110.0,
    'CAD': 1.25,
    'AUD': 1.35,
    'CHF': 0.92,
    'CNY': 6.45,
    'INR': 74.5,
    'BRL': 5.2,
    'MXN': 20.1,
    'KRW': 1150.0,
    'SGD': 1.35,
    'HKD': 7.78,
    'SEK': 8.65,
    'NOK': 8.45,
    'DKK': 6.35,
    'PLN': 3.85,
    'CZK': 21.5,
    'HUF': 300.0
}

def add(a, b):
    """Return the sum of a and b."""
    return a + b

def subtract(a, b):
    """Return the difference of a and b."""
    return a - b

def multiply(a, b):
    """Return the product of a and b."""
    return a * b

def divide(a, b):
    """Return the quotient of a and b. Raises ValueError on division by zero."""
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b

def power(a, b):
    """Return a raised to the power of b."""
    return a ** b

def modulus(a, b):
    """Return the remainder of a divided by b."""
    if b == 0:
        raise ValueError("Cannot take modulus by zero")
    return a % b

def sqrt(a):
    """Return the square root of a. Raises ValueError if a is negative."""
    if a < 0:
        raise ValueError("Cannot take square root of negative number")
    return math.sqrt(a)

def factorial(a):
    """Return the factorial of a. Raises ValueError if a is negative or not integer."""
    if not isinstance(a, int) or a < 0:
        raise ValueError("Factorial is only defined for non-negative integers")
    return math.factorial(a)

def average(*args):
    """Return the average of the given numbers."""
    if not args:
        raise ValueError("At least one number is required")
    return sum(args) / len(args)

def maximum(*args):
    """Return the maximum of the given numbers."""
    if not args:
        raise ValueError("At least one number is required")
    return max(args)

def minimum(*args):
    """Return the minimum of the given numbers."""
    if not args:
        raise ValueError("At least one number is required")
    return min(args)

def product(*args):
    """Return the product of the given numbers."""
    if not args:
        raise ValueError("At least one number is required")
    return reduce(operator.mul, args, 1)

def abs_val(a):
    """Return the absolute value of a."""
    return abs(a)

def reciprocal(a):
    """Return the reciprocal of a. Raises ValueError if a is zero."""
    if a == 0:
        raise ValueError("Cannot take reciprocal of zero")
    return 1 / a

def log(a, base=math.e):
    """Return the logarithm of a to the given base. Raises ValueError if a <= 0."""
    if a <= 0:
        raise ValueError("Logarithm only defined for positive numbers")
    return math.log(a, base)

def exp(a):
    """Return e raised to the power of a."""
    return math.exp(a)

def round_number(a, ndigits=0):
    """Return a rounded to ndigits decimal places."""
    return round(a, ndigits)

# Trigonometric Functions
def sin(angle, degrees=False):
    """Return the sine of angle. If degrees=True, angle is in degrees, otherwise radians."""
    if degrees:
        angle = math.radians(angle)
    return math.sin(angle)

def cos(angle, degrees=False):
    """Return the cosine of angle. If degrees=True, angle is in degrees, otherwise radians."""
    if degrees:
        angle = math.radians(angle)
    return math.cos(angle)

def tan(angle, degrees=False):
    """Return the tangent of angle. If degrees=True, angle is in degrees, otherwise radians."""
    if degrees:
        angle = math.radians(angle)
    return math.tan(angle)

def asin(value):
    """Return the arcsine of value in radians."""
    if not -1 <= value <= 1:
        raise ValueError("Arcsine is only defined for values between -1 and 1")
    return math.asin(value)

def acos(value):
    """Return the arccosine of value in radians."""
    if not -1 <= value <= 1:
        raise ValueError("Arccosine is only defined for values between -1 and 1")
    return math.acos(value)

def atan(value):
    """Return the arctangent of value in radians."""
    return math.atan(value)

def atan2(y, x):
    """Return the arctangent of y/x in radians, taking into account the quadrant."""
    return math.atan2(y, x)

def sinh(x):
    """Return the hyperbolic sine of x."""
    return math.sinh(x)

def cosh(x):
    """Return the hyperbolic cosine of x."""
    return math.cosh(x)

def tanh(x):
    """Return the hyperbolic tangent of x."""
    return math.tanh(x)

def degrees_to_radians(degrees):
    """Convert degrees to radians."""
    return math.radians(degrees)

def radians_to_degrees(radians):
    """Convert radians to degrees."""
    return math.degrees(radians)

# Foreign Exchange Functions
def get_exchange_rates() -> Dict[str, float]:
    """
    Get current exchange rates. In a production environment, this would fetch live rates.
    For now, returns default rates.
    """
    try:
        # You can replace this with a real API call to get live rates
        # Example: response = requests.get('https://api.exchangerate-api.com/v4/latest/USD')
        # return response.json()['rates']
        return DEFAULT_EXCHANGE_RATES.copy()
    except Exception:
        return DEFAULT_EXCHANGE_RATES.copy()

def convert_currency(amount: float, from_currency: str, to_currency: str, 
                    rates: Optional[Dict[str, float]] = None) -> float:
    """
    Convert amount from one currency to another.
    
    Args:
        amount: The amount to convert
        from_currency: The source currency code (e.g., 'USD', 'EUR')
        to_currency: The target currency code (e.g., 'USD', 'EUR')
        rates: Optional exchange rates dictionary. If None, uses default rates.
    
    Returns:
        The converted amount
    
    Raises:
        ValueError: If currency codes are not supported
    """
    if rates is None:
        rates = get_exchange_rates()
    
    from_currency = from_currency.upper()
    to_currency = to_currency.upper()
    
    if from_currency not in rates:
        raise ValueError(f"Unsupported currency: {from_currency}")
    if to_currency not in rates:
        raise ValueError(f"Unsupported currency: {to_currency}")
    
    # Convert to USD first (base currency), then to target currency
    usd_amount = amount / rates[from_currency]
    return usd_amount * rates[to_currency]

def get_currency_list() -> list:
    """Return a list of supported currency codes."""
    return list(DEFAULT_EXCHANGE_RATES.keys())

def calculate_currency_spread(buy_rate: float, sell_rate: float) -> float:
    """
    Calculate the spread between buy and sell rates.
    
    Args:
        buy_rate: The rate at which you can buy the currency
        sell_rate: The rate at which you can sell the currency
    
    Returns:
        The spread as a percentage
    """
    if buy_rate <= 0 or sell_rate <= 0:
        raise ValueError("Rates must be positive")
    
    return ((sell_rate - buy_rate) / buy_rate) * 100

def calculate_compound_interest(principal: float, rate: float, time: float, 
                               compounds_per_year: int = 1) -> float:
    """
    Calculate compound interest.
    
    Args:
        principal: Initial amount
        rate: Annual interest rate (as decimal, e.g., 0.05 for 5%)
        time: Time in years
        compounds_per_year: Number of times interest is compounded per year
    
    Returns:
        Final amount after compound interest
    """
    return principal * (1 + rate / compounds_per_year) ** (compounds_per_year * time)

def calculate_simple_interest(principal: float, rate: float, time: float) -> float:
    """
    Calculate simple interest.
    
    Args:
        principal: Initial amount
        rate: Annual interest rate (as decimal, e.g., 0.05 for 5%)
        time: Time in years
    
    Returns:
        Interest earned
    """
    return principal * rate * time

def calculate_loan_payment(principal: float, rate: float, time: float, 
                          payments_per_year: int = 12) -> float:
    """
    Calculate monthly loan payment using the standard loan payment formula.
    
    Args:
        principal: Loan amount
        rate: Annual interest rate (as decimal, e.g., 0.05 for 5%)
        time: Loan term in years
        payments_per_year: Number of payments per year (default 12 for monthly)
    
    Returns:
        Payment amount per period
    """
    if rate == 0:
        return principal / (time * payments_per_year)
    
    r = rate / payments_per_year
    n = time * payments_per_year
    
    if r == 0:
        return principal / n
    
    return principal * (r * (1 + r) ** n) / ((1 + r) ** n - 1)

# Additional Mathematical Functions
def gcd(a: int, b: int) -> int:
    """Return the greatest common divisor of a and b."""
    return math.gcd(a, b)

def lcm(a: int, b: int) -> int:
    """Return the least common multiple of a and b."""
    return abs(a * b) // math.gcd(a, b)

def is_prime(n: int) -> bool:
    """Check if a number is prime."""
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        if n % i == 0:
            return False
    return True

def fibonacci(n: int) -> int:
    """Return the nth Fibonacci number."""
    if n < 0:
        raise ValueError("Fibonacci is only defined for non-negative integers")
    if n <= 1:
        return n
    
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b

def binomial_coefficient(n: int, k: int) -> int:
    """Return the binomial coefficient C(n,k)."""
    if k < 0 or k > n:
        return 0
    if k == 0 or k == n:
        return 1
    
    # Use the formula C(n,k) = n! / (k! * (n-k)!)
    return math.factorial(n) // (math.factorial(k) * math.factorial(n - k))
