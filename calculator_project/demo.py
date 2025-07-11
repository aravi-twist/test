#!/usr/bin/env python3
"""
Demo script showcasing the enhanced calculator with trigonometric and foreign exchange features.
"""

from calculator import *

def demo_basic_operations():
    """Demonstrate basic arithmetic operations."""
    print("=== Basic Arithmetic Operations ===")
    print(f"Addition: 5 + 3 = {add(5, 3)}")
    print(f"Subtraction: 10 - 4 = {subtract(10, 4)}")
    print(f"Multiplication: 6 × 7 = {multiply(6, 7)}")
    print(f"Division: 15 ÷ 3 = {divide(15, 3)}")
    print(f"Power: 2^8 = {power(2, 8)}")
    print(f"Square root: √16 = {sqrt(16)}")
    print(f"Factorial: 5! = {factorial(5)}")
    print()

def demo_trigonometric_functions():
    """Demonstrate trigonometric functions."""
    print("=== Trigonometric Functions ===")
    
    # Basic trig functions in degrees
    angle_deg = 30
    print(f"sin({angle_deg}°) = {sin(angle_deg, degrees=True):.4f}")
    print(f"cos({angle_deg}°) = {cos(angle_deg, degrees=True):.4f}")
    print(f"tan({angle_deg}°) = {tan(angle_deg, degrees=True):.4f}")
    
    # Inverse trig functions
    value = 0.5
    print(f"arcsin({value}) = {asin(value):.4f} radians = {radians_to_degrees(asin(value)):.2f}°")
    print(f"arccos({value}) = {acos(value):.4f} radians = {radians_to_degrees(acos(value)):.2f}°")
    print(f"arctan({value}) = {atan(value):.4f} radians = {radians_to_degrees(atan(value)):.2f}°")
    
    # Hyperbolic functions
    x = 1.5
    print(f"sinh({x}) = {sinh(x):.4f}")
    print(f"cosh({x}) = {cosh(x):.4f}")
    print(f"tanh({x}) = {tanh(x):.4f}")
    
    # Angle conversions
    degrees = 180
    radians = math.pi
    print(f"{degrees}° = {degrees_to_radians(degrees):.4f} radians")
    print(f"{radians} radians = {radians_to_degrees(radians):.2f}°")
    print()

def demo_foreign_exchange():
    """Demonstrate foreign exchange calculations."""
    print("=== Foreign Exchange Calculations ===")
    
    # Currency conversion
    amount = 100
    from_curr = "USD"
    to_curr = "EUR"
    converted = convert_currency(amount, from_curr, to_curr)
    print(f"{amount} {from_curr} = {converted:.2f} {to_curr}")
    
    # More conversions
    conversions = [
        (50, "USD", "GBP"),
        (1000, "EUR", "JPY"),
        (25, "CAD", "AUD"),
        (500, "USD", "INR")
    ]
    
    for amount, from_curr, to_curr in conversions:
        converted = convert_currency(amount, from_curr, to_curr)
        print(f"{amount} {from_curr} = {converted:.2f} {to_curr}")
    
    # Currency spread calculation
    buy_rate = 1.20
    sell_rate = 1.25
    spread = calculate_currency_spread(buy_rate, sell_rate)
    print(f"Currency spread: {spread:.2f}%")
    
    # Available currencies
    currencies = get_currency_list()
    print(f"Supported currencies: {', '.join(currencies[:10])}... (and {len(currencies)-10} more)")
    print()

def demo_financial_calculations():
    """Demonstrate financial calculations."""
    print("=== Financial Calculations ===")
    
    # Compound interest
    principal = 10000
    rate = 0.05  # 5%
    time = 5
    final_amount = calculate_compound_interest(principal, rate, time)
    print(f"Compound interest: ${principal} at {rate*100}% for {time} years = ${final_amount:.2f}")
    
    # Monthly compounding
    monthly_compounded = calculate_compound_interest(principal, rate, time, compounds_per_year=12)
    print(f"Monthly compounded: ${monthly_compounded:.2f}")
    
    # Simple interest
    simple_interest = calculate_simple_interest(principal, rate, time)
    print(f"Simple interest earned: ${simple_interest:.2f}")
    
    # Loan payment calculation
    loan_amount = 200000
    loan_rate = 0.04  # 4%
    loan_term = 30
    monthly_payment = calculate_loan_payment(loan_amount, loan_rate, loan_term)
    print(f"Monthly loan payment: ${monthly_payment:.2f} for ${loan_amount:,} loan at {loan_rate*100}% for {loan_term} years")
    print()

def demo_advanced_math():
    """Demonstrate advanced mathematical functions."""
    print("=== Advanced Mathematical Functions ===")
    
    # GCD and LCM
    a, b = 48, 18
    print(f"GCD({a}, {b}) = {gcd(a, b)}")
    print(f"LCM({a}, {b}) = {lcm(a, b)}")
    
    # Prime number check
    numbers = [2, 3, 4, 17, 25, 29, 100]
    for num in numbers:
        prime_status = "prime" if is_prime(num) else "not prime"
        print(f"{num} is {prime_status}")
    
    # Fibonacci numbers
    print("Fibonacci sequence (first 10):", end=" ")
    for i in range(10):
        print(fibonacci(i), end=" ")
    print()
    
    # Binomial coefficient
    n, k = 5, 2
    print(f"Binomial coefficient C({n},{k}) = {binomial_coefficient(n, k)}")
    
    # Statistical functions
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print(f"Average of {numbers}: {average(*numbers)}")
    print(f"Maximum: {maximum(*numbers)}")
    print(f"Minimum: {minimum(*numbers)}")
    print(f"Product: {product(*numbers)}")
    print()

def demo_error_handling():
    """Demonstrate error handling."""
    print("=== Error Handling Examples ===")
    
    try:
        divide(10, 0)
    except ValueError as e:
        print(f"Error caught: {e}")
    
    try:
        sqrt(-4)
    except ValueError as e:
        print(f"Error caught: {e}")
    
    try:
        convert_currency(100, "USD", "XYZ")
    except ValueError as e:
        print(f"Error caught: {e}")
    
    try:
        asin(2)
    except ValueError as e:
        print(f"Error caught: {e}")
    
    print()

def main():
    """Run all demonstrations."""
    print("🧮 Enhanced Calculator Demo")
    print("=" * 50)
    print()
    
    demo_basic_operations()
    demo_trigonometric_functions()
    demo_foreign_exchange()
    demo_financial_calculations()
    demo_advanced_math()
    demo_error_handling()
    
    print("🎉 Demo completed! The calculator now supports:")
    print("• Basic arithmetic operations")
    print("• Trigonometric functions (sin, cos, tan, inverse, hyperbolic)")
    print("• Foreign exchange conversions")
    print("• Financial calculations (interest, loans)")
    print("• Advanced mathematical functions (GCD, LCM, primes, Fibonacci)")
    print("• Comprehensive error handling")

if __name__ == "__main__":
    main() 