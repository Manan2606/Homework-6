'''Main file for the calculator application.

This script provides a command-line interface for performing basic arithmetic operations.
'''

import sys
from decimal import Decimal, InvalidOperation
from calculator import Calculator  # Assuming Calculator is defined as shown previously

class OperationCommand:
    '''Operation command class for executing arithmetic operations.'''
    # pylint: disable=too-few-public-methods

    def __init__(self, calculator, operation_name, a, b):
        self.calculator = calculator
        self.operation_name = operation_name
        self.a = a
        self.b = b

    def execute(self):
        '''Execute the arithmetic operation.'''
        operation_method = getattr(self.calculator, self.operation_name, None)
        if operation_method:
            return operation_method(self.a, self.b)
        raise ValueError(f"Unknown operation: {self.operation_name}")

def calculate_and_print(a, b, operation_name):
    '''Calculate the result of the given operation and print it.

    Args:
        a (str): The first number as a string.
        b (str): The second number as a string.
        operation_name (str): The name of the operation to perform.
    '''
    try:
        a_decimal, b_decimal = map(Decimal, [a, b])
        command = OperationCommand(Calculator(), operation_name, a_decimal, b_decimal)
        result = command.execute()
        print(f"The result of {a} {operation_name} {b} is equal to {result}")
    except InvalidOperation:
        print(f"Invalid number input: {a} or {b} is not a valid number.")
    except ZeroDivisionError:
        print("Error: Division by zero.")
    except ValueError as e:
        print(e)
    except (TypeError, AttributeError) as e:  # Catch more specific exceptions
        print(f"An error occurred: {e}")

def main():
    '''Main function to handle command line input.'''
    if len(sys.argv) != 4:
        print("Usage: python calculator_main.py <number1> <number2> <operation>")
        sys.exit(1)

    _, a, b, operation_name = sys.argv
    calculate_and_print(a, b, operation_name)

if __name__ == '__main__':
    main()
