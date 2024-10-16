'''test_app.py'''
import pytest
from app import App
from app.commands.arithmetic import AddCommand, SubtractCommand, MultiplyCommand, DivideCommand


@pytest.fixture
def app():
    """Create an instance of the App class for testing."""
    return App()


def test_app_get_environment_variable(app):
    """Test that the application retrieves the correct environment variable."""
    current_env = app.get_environment_variable('ENVIRONMENT')
    assert current_env in ['DEVELOPMENT', 'TESTING', 'PRODUCTION'], f"Invalid ENVIRONMENT: {current_env}"


def test_app_start_exit_command(monkeypatch, app):
    """Test that the REPL exits correctly on 'exit' command."""
    monkeypatch.setattr('builtins.input', lambda _: 'exit')
    with pytest.raises(SystemExit) as e:
        app.start()
    assert e.type == SystemExit


def test_app_start_unknown_command(monkeypatch, capfd, app):
    """Test how the REPL handles an unknown command before exiting."""
    inputs = iter(['unknown_command', 'exit'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    with pytest.raises(SystemExit):
        app.start()

    captured = capfd.readouterr()
    assert "No such command: unknown_command" in captured.out


def test_app_register_commands(app):
    """Test registering command classes in the command handler."""
    app.command_handler.register_command('add', AddCommand)
    app.command_handler.register_command('subtract', SubtractCommand)

    assert 'add' in app.command_handler.commands
    assert 'subtract' in app.command_handler.commands


def test_add_command_execution(capfd):
    """Test execution of the AddCommand."""
    command = AddCommand(3, 5)
    command.execute()
    captured = capfd.readouterr()
    assert "The result of adding 3 and 5 is 8" in captured.out


def test_subtract_command_execution(capfd):
    """Test execution of the SubtractCommand."""
    command = SubtractCommand(10, 4)
    command.execute()
    captured = capfd.readouterr()
    assert "The result of subtracting 4 from 10 is 6" in captured.out


def test_multiply_command_execution(capfd):
    """Test execution of the MultiplyCommand."""
    command = MultiplyCommand(2, 3)
    command.execute()
    captured = capfd.readouterr()
    assert "The result of multiplying 2 and 3 is 6" in captured.out


def test_divide_command_execution(capfd):
    """Test execution of the DivideCommand."""
    command = DivideCommand(8, 2)
    command.execute()
    captured = capfd.readouterr()
    assert "The result of dividing 8 by 2 is 4.0" in captured.out


def test_divide_command_execution_by_zero(capfd):
    """Test handling of division by zero in DivideCommand."""
    command = DivideCommand(8, 0)
    command.execute()
    captured = capfd.readouterr()
    assert "Cannot divide by zero" in captured.out
