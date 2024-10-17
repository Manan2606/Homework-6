from abc import ABC, abstractmethod

class Command(ABC):
    @abstractmethod
    def execute(self):
        pass

class CommandHandler:
    def __init__(self):
        self.commands = {}

    def register_command(self, name, command):
        """Register a command with a name."""
        self.commands[name] = command

    def execute_command(self, command_name, *args):
        """Execute a command by name, passing any arguments to it."""
        command = self.commands.get(command_name)
        if command is not None:
            return command.execute(*args)  # Pass the args to the command's execute method
        raise KeyError(f"No such command: {command_name}")

