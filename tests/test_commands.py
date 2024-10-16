'''test_commands.py'''
import pytest
from app import App

def test_app_greet_command(capfd, monkeypatch):
    """Test that the REPL correctly handles the 'greet' command."""
    # Simulate user entering 'greet' followed by 'exit'
    inputs = iter(['greet', 'exit'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    app = App()
    with pytest.raises(SystemExit) as e:
        app.start()  # Assuming App.start() is now a static method

    assert str(e.value) == "Exiting...", "The app did not exit as expected"

    # Verify the output for the 'greet' command
    captured = capfd.readouterr()
    assert "Hello, World!" in captured.out

def test_app_unknown_command(capfd, monkeypatch):
    """Test that the REPL correctly handles an unknown command."""
    # Simulate user entering an unknown command followed by 'exit'
    inputs = iter(['unknown_command', 'exit'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    app = App()
    with pytest.raises(SystemExit) as e:
        app.start()

    assert str(e.value) == "Exiting...", "The app did not exit as expected"

    # Verify the output for the unknown command
    captured = capfd.readouterr()
    assert "No such command: unknown_command" in captured.out

def test_app_exit_command(capfd, monkeypatch):
    """Test that the REPL correctly handles the 'exit' command."""
    # Simulate user entering 'exit' immediately
    monkeypatch.setattr('builtins.input', lambda _: 'exit')

    app = App()
    with pytest.raises(SystemExit) as e:
        app.start()

    assert str(e.value) == "Exiting...", "The app did not exit as expected"

def test_app_goodbye_command(capfd, monkeypatch):
    """Test that the REPL correctly handles the 'goodbye' command."""
    # Simulate user entering 'goodbye' followed by 'exit'
    inputs = iter(['goodbye', 'exit'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    app = App()
    with pytest.raises(SystemExit) as e:
        app.start()

    assert str(e.value) == "Exiting...", "The app did not exit as expected"

    # Verify the output for the 'goodbye' command
    captured = capfd.readouterr()
    assert "Goodbye" in captured.out

def test_app_hello_command(capfd, monkeypatch):
    """Test that the REPL correctly handles the 'hello' command."""
    # Simulate user entering 'hello' followed by 'exit'
    inputs = iter(['hello', 'exit'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    app = App()
    with pytest.raises(SystemExit) as e:
        app.start()

    assert str(e.value) == "Exiting...", "The app did not exit as expected"

    # Verify the output for the 'hello' command
    captured = capfd.readouterr()
    assert "Hello" in captured.out
