'''test_app.py'''
from unittest.mock import MagicMock
import pytest
from app import App, CommandHandler

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

def test_command_handler_register_command():
    """Test command registration."""
    command_handler = CommandHandler()
    mock_command = MagicMock()

    command_handler.register_command("mock", mock_command)
    assert "mock" in command_handler.commands
    assert command_handler.commands["mock"] == mock_command

def test_command_handler_execute_command_valid():
    """Test executing a valid command."""
    command_handler = CommandHandler()
    mock_command = MagicMock()
    mock_command.execute.return_value = "Executed"

    command_handler.register_command("mock", mock_command)
    result = command_handler.execute_command("mock")

    assert result == "Executed"
    mock_command.execute.assert_called_once()

def test_command_handler_execute_command_invalid():
    """Test executing an invalid command."""
    command_handler = CommandHandler()

    with pytest.raises(KeyError):
        command_handler.execute_command("invalid_command")
