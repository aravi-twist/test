# Enhanced Calculator

A comprehensive Python calculator module that provides basic arithmetic operations, trigonometric functions, foreign exchange calculations, and advanced mathematical utilities.

## Features

### 🧮 Basic Arithmetic
- Addition, subtraction, multiplication, division
- Power and square root operations
- Modulus and factorial calculations
- Statistical functions (average, min, max, product)

### 📐 Trigonometric Functions
- **Basic Trig**: `sin()`, `cos()`, `tan()` (supports both degrees and radians)
- **Inverse Trig**: `asin()`, `acos()`, `atan()`, `atan2()`
- **Hyperbolic**: `sinh()`, `cosh()`, `tanh()`
- **Angle Conversions**: degrees ↔ radians

### 💱 Foreign Exchange
- Currency conversion between 20+ major currencies
- Support for USD, EUR, GBP, JPY, CAD, AUD, CHF, CNY, INR, and more
- Currency spread calculations
- Extensible for live rate APIs

### 💰 Financial Calculations
- Compound interest (with customizable compounding periods)
- Simple interest calculations
- Loan payment calculations (monthly payments)
- Investment growth projections

### 🔢 Advanced Mathematics
- Greatest Common Divisor (GCD) and Least Common Multiple (LCM)
- Prime number detection
- Fibonacci sequence generation
- Binomial coefficients
- Logarithmic and exponential functions

## Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd calculator_project
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

## Usage

### Basic Operations
```python
from calculator import add, subtract, multiply, divide, power, sqrt

# Basic arithmetic
result = add(5, 3)  # 8
result = multiply(6, 7)  # 42
result = power(2, 8)  # 256
result = sqrt(16)  # 4.0
```

### Trigonometric Functions
```python
from calculator import sin, cos, tan, asin, degrees_to_radians

# Trig functions (degrees)
angle = 30
sin_30 = sin(angle, degrees=True)  # 0.5
cos_30 = cos(angle, degrees=True)  # 0.8660...

# Inverse trig
value = 0.5
angle_rad = asin(value)  # 0.5236 radians
angle_deg = degrees_to_radians(asin(value))  # 30.0 degrees
```

### Foreign Exchange
```python
from calculator import convert_currency, get_currency_list

# Currency conversion
usd_to_eur = convert_currency(100, "USD", "EUR")  # ~85.0 EUR
eur_to_jpy = convert_currency(1000, "EUR", "JPY")  # ~129,411.76 JPY

# Get supported currencies
currencies = get_currency_list()
print(f"Supported: {currencies}")
```

### Financial Calculations
```python
from calculator import calculate_compound_interest, calculate_loan_payment

# Compound interest
principal = 10000
rate = 0.05  # 5%
time = 5
final_amount = calculate_compound_interest(principal, rate, time)

# Loan payment
loan_amount = 200000
loan_rate = 0.04  # 4%
loan_term = 30
monthly_payment = calculate_loan_payment(loan_amount, loan_rate, loan_term)
```

### Advanced Math
```python
from calculator import gcd, lcm, is_prime, fibonacci

# Number theory
result = gcd(48, 18)  # 6
result = lcm(12, 18)  # 36
is_17_prime = is_prime(17)  # True

# Sequences
fib_10 = fibonacci(10)  # 55
```

## Demo

Run the demo script to see all features in action:

```bash
python demo.py
```

This will showcase:
- Basic arithmetic operations
- Trigonometric functions with examples
- Foreign exchange conversions
- Financial calculations
- Advanced mathematical functions
- Error handling examples

## Supported Currencies

The calculator supports the following currencies:
- USD (US Dollar)
- EUR (Euro)
- GBP (British Pound)
- JPY (Japanese Yen)
- CAD (Canadian Dollar)
- AUD (Australian Dollar)
- CHF (Swiss Franc)
- CNY (Chinese Yuan)
- INR (Indian Rupee)
- BRL (Brazilian Real)
- MXN (Mexican Peso)
- KRW (South Korean Won)
- SGD (Singapore Dollar)
- HKD (Hong Kong Dollar)
- SEK (Swedish Krona)
- NOK (Norwegian Krone)
- DKK (Danish Krone)
- PLN (Polish Złoty)
- CZK (Czech Koruna)
- HUF (Hungarian Forint)

## Error Handling

The calculator includes comprehensive error handling:
- Division by zero
- Invalid mathematical operations (e.g., sqrt of negative numbers)
- Unsupported currency codes
- Invalid input ranges for trigonometric functions
- Type validation for factorial and other functions

## Extending the Calculator

### Adding Live Exchange Rates

To use live exchange rates instead of default rates, modify the `get_exchange_rates()` function:

```python
def get_exchange_rates():
    try:
        response = requests.get('https://api.exchangerate-api.com/v4/latest/USD')
        return response.json()['rates']
    except Exception:
        return DEFAULT_EXCHANGE_RATES.copy()
```

### Adding New Functions

You can easily extend the calculator by adding new mathematical functions to the module.

## Testing

Run the demo script to test all functionality:

```bash
python demo.py
```

## Contributing

1. Fork the repository
2. Create a feature branch
3. Add your enhancements
4. Test thoroughly
5. Submit a pull request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- Built with Python's built-in `math` module
- Exchange rates are approximate and should be updated for production use
- Inspired by scientific calculators and financial tools