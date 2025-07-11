"""
A more advanced calculator module providing basic and advanced arithmetic operations.
"""

import math
import operator
from functools import reduce

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
