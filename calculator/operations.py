"""
This module defines basic arithmetic operations for Decimal types.
It includes functions for addition, subtraction, multiplication, and division.
"""
from decimal import Decimal
# Define the functions with type hints
# pylint: disable=unnecessary-dunder-call, invalid-name
def add(a: Decimal, b: Decimal) -> Decimal:
    """Return the sum of a and b."""
    return a + b

def subtract(a: Decimal, b: Decimal) -> Decimal:
    """Return the difference of a and b."""
    return a - b

def multiply(a: Decimal, b: Decimal) -> Decimal:
    """Return the product of a and b."""
    return a * b

def divide(a: Decimal, b: Decimal) -> Decimal:
    """Return the quotient of a and b. Raises ValueError if b is zero."""
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b
