'''test_plugiin_greet.py'''
import pytest
from app import App

def test_app_greet_command(capfd, monkeypatch):
    """Test that the REPL correctly handles the 'greet' command and outputs 'Hello, World!'."""
    inputs = iter(['greet', 'exit'])  # Simulate user input
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))  # Mock input

    app = App()
    with pytest.raises(SystemExit):
        app.start()  # Start the application

    # Capture the output after processing input commands
    out, err = capfd.readouterr()  # err is captured but not used  # pylint: disable=unused-variable

    # Check that the exit message was printed
    assert "Exiting..." in out, "Exit message not printed."

    # Assert that 'Hello, World!' was printed to stdout
    assert "Hello, World!" in out, "The 'greet' command did not produce the expected output."
