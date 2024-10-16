# app.py
from commands import CommandHandler
from commands.arithmetic import AddCommand, SubtractCommand, MultiplyCommand, DivideCommand
from commands.greet import GreetCommand
from commands.goodbye import GoodbyeCommand

class App:
    def __init__(self):
        self.handler = CommandHandler()
        self.register_commands()

    def register_commands(self):
        self.handler.register_command("greet", GreetCommand)
        self.handler.register_command("goodbye", GoodbyeCommand)
        self.handler.register_command("add", AddCommand)
        self.handler.register_command("subtract", SubtractCommand)
        self.handler.register_command("multiply", MultiplyCommand)
        self.handler.register_command("divide", DivideCommand)

    def start(self):
        print("Welcome to the interactive calculator. Type 'exit' to quit.")
        while True:
            command = input("Enter a command: ").strip().lower()
            if command == "exit":
                raise SystemExit("Exiting...")
            self.handler.execute_command(command)
