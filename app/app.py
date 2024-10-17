from app.commands import CommandHandler
from app.plugins.add import AddCommand
from app.plugins.subtract import SubtractCommand
from app.plugins.multiply import MultiplyCommand
from app.plugins.divide import DivideCommand

class App:
    def __init__(self):
        self.command_handler = CommandHandler()
        self.command_handler.register_command("add", AddCommand())
        self.command_handler.register_command("subtract", SubtractCommand())
        self.command_handler.register_command("multiply", MultiplyCommand())
        self.command_handler.register_command("divide", DivideCommand())

    def execute_with_args(self, command_name, *args):
        """Wrapper to pass arguments to the command's execute method"""
        command = self.command_handler.commands.get(command_name)
        if command:
            return command.execute(*args)
        else:
            return f"No such command: {command_name}"
