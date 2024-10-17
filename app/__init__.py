import os
import pkgutil
import importlib
from app.commands import CommandHandler, Command
from app.plugins.add import AddCommand
from app.plugins.subtract import SubtractCommand
from app.plugins.multiply import MultiplyCommand
from app.plugins.divide import DivideCommand
from dotenv import load_dotenv
import logging
import logging.config

class App:
    def __init__(self):
        """Initialize the application, configure logging, and load environment variables."""
        os.makedirs('logs', exist_ok=True)  # Ensure the logs directory exists
        self.configure_logging()
        load_dotenv()  # Load environment variables from .env file
        self.settings = self.load_environment_variables()
        self.settings.setdefault('ENVIRONMENT', 'PRODUCTION')  # Set default environment
        self.command_handler = CommandHandler()  # Initialize command handler
        self.command_handler.register_command("add", AddCommand())
        self.command_handler.register_command("subtract", SubtractCommand())
        self.command_handler.register_command("multiply", MultiplyCommand())
        self.command_handler.register_command("divide", DivideCommand())

    def configure_logging(self):
        """Configure logging for the application."""
        logging_conf_path = 'logging.conf'
        if os.path.exists(logging_conf_path):
            logging.config.fileConfig(logging_conf_path, disable_existing_loggers=False)
        else:
            logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
        logging.info("Logging configured.")

    def load_environment_variables(self):
        """Load environment variables into the application's settings."""
        settings = {key: value for key, value in os.environ.items()}
        logging.info("Environment variables loaded.")
        return settings

    def get_environment_variable(self, env_var: str = 'ENVIRONMENT'):
        """Retrieve an environment variable from settings."""
        return self.settings.get(env_var, None)

    def load_plugins(self):
        """Load plugins from the specified plugins directory."""
        plugins_package = 'app.plugins'
        plugins_path = plugins_package.replace('.', '/')
        if not os.path.exists(plugins_path):
            logging.warning(f"Plugins directory '{plugins_path}' not found.")
            return
        for _, plugin_name, is_pkg in pkgutil.iter_modules([plugins_path]):
            if is_pkg:
                try:
                    plugin_module = importlib.import_module(f'{plugins_package}.{plugin_name}')
                    self.register_plugin_commands(plugin_module, plugin_name)
                except ImportError as e:
                    logging.error(f"Error importing plugin {plugin_name}: {e}")

    def register_plugin_commands(self, plugin_module, plugin_name):
        """Register command classes from a plugin module with the command handler."""
        for item_name in dir(plugin_module):
            item = getattr(plugin_module, item_name)
            if isinstance(item, type) and issubclass(item, Command) and item is not Command:
                self.command_handler.register_command(plugin_name, item())
                logging.info(f"Command '{plugin_name}' from plugin '{plugin_name}' registered.")

    def start(self):
        """Start the REPL for command input."""
        self.load_plugins()
        logging.info("Application started. Type 'exit' to exit.")
        try:
            while True:
                cmd_input = input(">>> ").strip()
                if cmd_input.lower() == 'exit':
                    print("Exiting...")
                    logging.info("Application exit.")
                    raise SystemExit("Exiting...")

                # Handle commands that require additional arguments
                if cmd_input in ["add", "subtract", "multiply", "divide"]:
                    try:
                        a = float(input("Enter the first number: ").strip())
                        b = float(input("Enter the second number: ").strip())
                        result = self.command_handler.execute_command(cmd_input, a, b)
                        print(result)
                    except ValueError:
                        logging.error("Invalid input for numbers.")
                        print("Please enter valid numbers.")
                    except Exception as e:
                        logging.error(f"Error executing command '{cmd_input}': {e}")
                        print(f"Error: {e}")
                else:
                    try:
                        result = self.command_handler.execute_command(cmd_input)
                        if result:
                            print(result)
                    except KeyError:
                        logging.error(f"Unknown command: {cmd_input}")
                        print(f"No such command: {cmd_input}")
        except KeyboardInterrupt:
            logging.info("Application interrupted and exiting gracefully.")
            raise SystemExit("Exiting...")
        finally:
            logging.info("Application shutdown.")

    def execute_with_args(self, command_name, *args):
        """Execute a command with the given arguments.

        Args:
            command_name (str): The name of the command to execute.
            *args: Arguments to pass to the command.

        Returns:
            str: The result of the command execution.
        """
        try:
            return self.command_handler.execute_command(command_name, *args)
        except KeyError:
            logging.error(f"Unknown command: {command_name}")
            return f"No such command: {command_name}"

if __name__ == "__main__":
    app = App()
    app.start()
