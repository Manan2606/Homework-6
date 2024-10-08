import sys
from app.commands import Command


class HelloCommand(Command):
    def execute(self):
        print(f'Hello')