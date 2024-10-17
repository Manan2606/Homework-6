from app.commands import Command
from decimal import Decimal, InvalidOperation

class DivideCommand(Command):
    def execute(self, *args):
        a, b = args
        try:
            a_decimal, b_decimal = map(Decimal, [a, b])
            if b_decimal == 0:
                return "An error occurred: Cannot divide by zero"
            return f"The result of {a} divide {b} is equal to {a_decimal / b_decimal}"
        except InvalidOperation:
            return f"Invalid number input: {a} or {b} is not a valid number."
