from app.commands import Command

class AddCommand(Command):
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def execute(self):
        result = self.num1 + self.num2
        print(f"The result of adding {self.num1} and {self.num2} is {result}")


class SubtractCommand(Command):
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def execute(self):
        result = self.num1 - self.num2
        print(f"The result of subtracting {self.num2} from {self.num1} is {result}")


class MultiplyCommand(Command):
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def execute(self):
        result = self.num1 * self.num2
        print(f"The result of multiplying {self.num1} and {self.num2} is {result}")


class DivideCommand(Command):
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def execute(self):
        if self.num2 == 0:
            print("Cannot divide by zero")
        else:
            result = self.num1 / self.num2
            print(f"The result of dividing {self.num1} by {self.num2} is {result}")
