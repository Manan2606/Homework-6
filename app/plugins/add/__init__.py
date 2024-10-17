from app.commands import Command
from decimal import Decimal, InvalidOperation

class AddCommand(Command):
    def execute(self, *args):
        a, b = args
        try:
            a_decimal, b_decimal = map(Decimal, [a, b])
            return f"The result of {a} add {b} is equal to {a_decimal + b_decimal}"
        except InvalidOperation:
            return f"Invalid number input: {a} or {b} is not a valid number."
