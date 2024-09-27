'''conftest file'''
# conftest.py
from decimal import Decimal
from faker import Faker
from calculator.operations import add, subtract, multiply, divide

fake = Faker()

def generate_test_data(num_records):
    """Generate test data for arithmetic operations.

    Args:
        num_records (int): The number of records to generate.

    Yields:
        tuple: A tuple containing two decimal numbers, operation name,
               operation function, and the expected result.
    """
    # Define operation mappings for both Calculator and Calculation tests
    operation_mappings = {
        'add': add,
        'subtract': subtract,
        'multiply': multiply,
        'divide': divide
    }
    # Generate test data
    for _ in range(num_records):
        a = Decimal(fake.random_number(digits=2))
        b = (
            Decimal(fake.random_number(digits=2)) if _ % 4 != 3
            else Decimal(fake.random_number(digits=1))
        )
        operation_name = fake.random_element(elements=list(operation_mappings.keys()))
        operation_func = operation_mappings[operation_name]
        # Ensure valid division
        # pylint: disable=comparison-with-callable
        if operation_func == divide:
            b = Decimal('1') if b == Decimal('0') else b
        try:
            if operation_func == divide and b == Decimal('0'):
                expected = "ZeroDivisionError"
            else:
                expected = operation_func(a, b)
        except ZeroDivisionError:
            expected = "ZeroDivisionError"
        yield a, b, operation_name, operation_func, expected

def pytest_addoption(parser):
    """Add command line options for pytest.

    Args:
        parser: The pytest parser object to add options to.
    """
    parser.addoption("--num_records", action="store",
                     default=5, type=int, help="Number of test records to generate")

def pytest_generate_tests(metafunc):
    """Generate tests based on the provided pytest options.

    Args:
        metafunc: The metafunc object that provides access to the test function.
    """
    # Check if the test is expecting any of the dynamically generated fixtures
    if {"a", "b", "expected"}.intersection(set(metafunc.fixturenames)):
        num_records = metafunc.config.getoption("num_records")
        parameters = list(generate_test_data(num_records))
        # Modify parameters to fit test functions' expectations
        modified_parameters = [
            (a, b, op_name if 'operation_name' in metafunc.fixturenames else op_func, expected)
            for a, b, op_name, op_func, expected in parameters]
        metafunc.parametrize("a,b,operation,expected", modified_parameters)
