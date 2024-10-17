from app.commands import Command
from decimal import Decimal, InvalidOperation

class MultiplyCommand(Command):
    def execute(self, *args):
        a, b = args
        try:
            a_decimal, b_decimal = map(Decimal, [a, b])
            return f"The result of {a} multiply {b} is equal to {a_decimal * b_decimal}"
        except InvalidOperation:
            return f"Invalid number input: {a} or {b} is not a valid number."
