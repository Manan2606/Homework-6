"""
This module defines the Calculator class, which provides basic arithmetic operations (addition, subtraction, multiplication, and division) using the Decimal data type for high-precision arithmetic.

The Calculator class leverages the Calculation class to perform operations and the Calculations class to manage a history of all performed calculations. Each operation is defined as a static method that delegates to a private _perform_operation method.

Imports:
    - decimal.Decimal: For high-precision arithmetic operations.
    - typing.Callable: For type hinting callable objects.
    - calculator.calculations.Calculations: Manages the history of all calculations.
    - calculator.operations: Contains the basic arithmetic operations (add, subtract, multiply, divide).
    - calculator.calculation.Calculation: Represents a single calculation.
"""

# Standard imports
from decimal import Decimal  # For high-precision arithmetic
from typing import Callable  # For type hinting callable objects

# Local imports
from calculator.calculations import Calculations  # Manages history of calculations
from calculator.operations import add, subtract, multiply, divide  # Arithmetic operations
from calculator.calculation import Calculation  # Represents a single calculation

# Definition of the Calculator class
class Calculator:
    """A class that provides basic arithmetic operations using Decimals."""

    @staticmethod
    # pylint: disable=invalid-name
    # a (Decimal): The first operand.
    # b (Decimal): The second operand.
    def _perform_operation(a: Decimal, b: Decimal, operation: Callable[[Decimal, Decimal], Decimal]) -> Decimal:
        """
        Create and perform a calculation, then return the result.
        operation (Callable): A function that takes two Decimal operands and returns a Decimal result.
        Returns:
            Decimal: The result of the calculation.
        """
        # Create a Calculation object using the static create method, passing in operands and the operation
        calculation = Calculation.create(a, b, operation)
        # Add the calculation to the history managed by the Calculations class
        Calculations.add_calculation(calculation)
        # Perform the calculation and return the result
        return calculation.perform()

    @staticmethod
    # pylint: disable=invalid-name
    def add(a: Decimal, b: Decimal) -> Decimal:
        """
        Perform addition by delegating to the _perform_operation method with the add operation.

        Returns:
            Decimal: The result of adding a and b.
        """
        return Calculator._perform_operation(a, b, add)

    @staticmethod
    # pylint: disable=invalid-name
    def subtract(a: Decimal, b: Decimal) -> Decimal:
        """
        Perform subtraction by delegating to the _perform_operation method with the subtract operation.

        Returns:
            Decimal: The result of subtracting b from a.
        """
        return Calculator._perform_operation(a, b, subtract)

    @staticmethod
    # pylint: disable=invalid-name
    def multiply(a: Decimal, b: Decimal) -> Decimal:
        """
        Perform multiplication by delegating to the _perform_operation method with the multiply operation.

        Returns:
            Decimal: The result of multiplying a and b.
        """
        return Calculator._perform_operation(a, b, multiply)

    @staticmethod
    # pylint: disable=invalid-name
    def divide(a: Decimal, b: Decimal) -> Decimal:
        """
        Perform division by delegating to the _perform_operation method with the divide operation.

        Returns:
            Decimal: The result of dividing a by b.
        """
        return Calculator._perform_operation(a, b, divide)
