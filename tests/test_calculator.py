'''test_calculator.py'''
import pytest
from app import App

# Initialize the App instance
app = App()

def test_add():
    """Test the addition command."""
    output = app.execute_with_args("add", "5", "3")
    assert output == "The result of 5 add 3 is equal to 8"

def test_subtract():
    """Test the subtraction command."""
    output = app.execute_with_args("subtract", "10", "2")
    assert output == "The result of 10 subtract 2 is equal to 8"

def test_multiply():
    """Test the multiplication command."""
    output = app.execute_with_args("multiply", "4", "5")
    assert output == "The result of 4 multiply 5 is equal to 20"

def test_divide():
    """Test the division command."""
    output = app.execute_with_args("divide", "20", "4")
    assert output == "The result of 20 divide 4 is equal to 5"

def test_divide_by_zero():
    """Test division by zero."""
    output = app.execute_with_args("divide", "1", "0")
    assert output == "An error occurred: Cannot divide by zero"

def test_unknown_operation():
    """Test an unknown operation command."""
    output = app.execute_with_args("unknown", "9", "3")
    assert output == "No such command: unknown"

def test_invalid_input_a():
    """Test invalid input for the first number."""
    output = app.execute_with_args("add", "a", "3")
    assert output == "Invalid number input: a or 3 is not a valid number."

def test_invalid_input_b():
    """Test invalid input for the second number."""
    output = app.execute_with_args("subtract", "5", "b")
    assert output == "Invalid number input: 5 or b is not a valid number."

@pytest.mark.parametrize("first_number, second_number, operation, expected_result", [
    (5, 3, "add", "The result of 5 add 3 is equal to 8"),
    (10, 2, "subtract", "The result of 10 subtract 2 is equal to 8"),
    (4, 5, "multiply", "The result of 4 multiply 5 is equal to 20"),
    (20, 4, "divide", "The result of 20 divide 4 is equal to 5"),
    (1, 0, "divide", "An error occurred: Cannot divide by zero")
])
def test_generated_operations(first_number, second_number, operation, expected_result):
    """Test generated operations with different inputs."""
    output = app.execute_with_args(operation, str(first_number), str(second_number))
    assert output == expected_result

def test_divide_negative_numbers():
    """Test division with negative numbers."""
    output = app.execute_with_args("divide", "-20", "4")
    assert output == "The result of -20 divide 4 is equal to -5"

    output = app.execute_with_args("divide", "20", "-4")
    assert output == "The result of 20 divide -4 is equal to -5"

    output = app.execute_with_args("divide", "-20", "-4")
    assert output == "The result of -20 divide -4 is equal to 5"

def test_divide_large_numbers():
    """Test division with large numbers."""
    output = app.execute_with_args("divide", "1000000", "500000")
    assert output == "The result of 1000000 divide 500000 is equal to 2"

def test_divide_by_one():
    """Test division by one."""
    output = app.execute_with_args("divide", "100", "1")
    assert output == "The result of 100 divide 1 is equal to 100"

def test_divide_by_negative_one():
    """Test division by negative one."""
    output = app.execute_with_args("divide", "100", "-1")
    assert output == "The result of 100 divide -1 is equal to -100"

def test_divide_floats():
    """Test division with floating-point numbers."""
    output = app.execute_with_args("divide", "5.5", "2.2")
    assert output == "The result of 5.5 divide 2.2 is equal to 2.5"

def test_divide_non_numeric():
    """Test division with non-numeric inputs."""
    output = app.execute_with_args("divide", "five", "2")
    assert output == "Invalid number input: five or 2 is not a valid number."

    output = app.execute_with_args("divide", "10", "zero")
    assert output == "Invalid number input: 10 or zero is not a valid number."

def test_multiply_negative_numbers():
    """Test multiplication with negative numbers."""
    output = app.execute_with_args("multiply", "-4", "5")
    assert output == "The result of -4 multiply 5 is equal to -20"

    output = app.execute_with_args("multiply", "4", "-5")
    assert output == "The result of 4 multiply -5 is equal to -20"

    output = app.execute_with_args("multiply", "-4", "-5")
    assert output == "The result of -4 multiply -5 is equal to 20"

def test_multiply_with_zero():
    """Test multiplication with zero."""
    output = app.execute_with_args("multiply", "0", "5")
    assert output == "The result of 0 multiply 5 is equal to 0"

    output = app.execute_with_args("multiply", "5", "0")
    assert output == "The result of 5 multiply 0 is equal to 0"

    output = app.execute_with_args("multiply", "0", "0")
    assert output == "The result of 0 multiply 0 is equal to 0"

def test_multiply_large_numbers():
    """Test multiplication with large numbers."""
    output = app.execute_with_args("multiply", "10000", "50000")
    assert output == "The result of 10000 multiply 50000 is equal to 500000000"

def test_multiply_by_one():
    """Test multiplication by one."""
    output = app.execute_with_args("multiply", "100", "1")
    assert output == "The result of 100 multiply 1 is equal to 100"

def test_multiply_by_negative_one():
    """Test multiplication by negative one."""
    output = app.execute_with_args("multiply", "100", "-1")
    assert output == "The result of 100 multiply -1 is equal to -100"

def test_multiply_non_numeric():
    """Test multiplication with non-numeric inputs."""
    output = app.execute_with_args("multiply", "five", "2")
    assert output == "Invalid number input: five or 2 is not a valid number."

    output = app.execute_with_args("multiply", "10", "zero")
    assert output == "Invalid number input: 10 or zero is not a valid number."
