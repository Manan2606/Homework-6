"""
This module defines the Calculation class, which encapsulates a mathematical calculation
with two operands (operand_a, operand_b) and a higher-order operation function.
The Decimal type is used for high-precision arithmetic.
The Calculation class allows flexible operations by accepting the operation as a callable.
"""

# Import the Decimal class for precise decimal arithmetic
from decimal import Decimal
# Import Callable from typing to specify the operation as a callable type hint
from typing import Callable

# Definition of the Calculation class with type annotations for improved readability and safety
class Calculation:
    """Class that encapsulates a mathematical calculation."""
    # a (Decimal): The first operand.
    # b (Decimal): The second operand.
    # pylint: disable=unnecessary-dunder-call, invalid-name
    def __init__(self, a: Decimal, b: Decimal, operation: Callable[[Decimal, Decimal], Decimal]):
        """
        Initialize the Calculation instance.
        operation (Callable[[Decimal, Decimal], Decimal]): The operation to perform on the operands.
        """
        # Initialize the first operand of the calculation
        self.a = a
        # Initialize the second operand of the calculation
        self.b = b
        # Store the operation as a callable that takes two Decimals and returns a Decimal
        self.operation = operation

    @staticmethod
    def create(a: Decimal, b: Decimal, operation: Callable[[Decimal, Decimal], Decimal]):
        """
        Create a new instance of Calculation.
        operation (Callable[[Decimal, Decimal], Decimal]): The operation to perform on the operands.
        Returns:
            Calculation: A new Calculation instance initialized with the provided arguments.
        """
        return Calculation(a, b, operation)

    def perform(self) -> Decimal:
        """Perform the stored calculation and return the result."""
        return self.operation(self.a, self.b)

    def __repr__(self):
        """Return a simplified string representation of the calculation."""
        return f"Calculation({self.a}, {self.b}, {self.operation.__name__})"
