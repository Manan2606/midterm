"""
Main application module for executing various mathematical commands.

This module initializes the application, configures logging,
loads environment variables, and registers commands.
"""

import os
import sys
import logging
import logging.config
from dotenv import load_dotenv
from app.command import CommandHandler
from app.pluggin.add import AddCommand
from app.pluggin.subtract import SubtractCommand
from app.pluggin.multiply import MultiplyCommand
from app.pluggin.divide import DivideCommand
from app.pluggin.mean import MeanCommand
from app.pluggin.median import MedianCommand
from app.pluggin.standard_deviation import StandardDeviationCommand


class App:
    """Main application class to manage command execution."""

    def __init__(self):
        """Initialize the application, configure logging, and load environment variables."""
        os.makedirs('logs', exist_ok=True)  # Ensure the logs directory exists
        self.configure_logging()
        load_dotenv()  # Load environment variables from .env file
        self.settings = dict(os.environ)  # Use dict instead of comprehension
        self.settings.setdefault('ENVIRONMENT', 'PRODUCTION')  # Set default environment
        self.command_handler = CommandHandler()  # Initialize command handler
        self.register_commands()

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
        settings = dict(os.environ)  # This method is no longer needed since it's already done in __init__
        logging.info("Environment variables loaded.")
        return settings

    def get_environment_variable(self, key):
        """Get a specific environment variable from the settings."""
        return self.settings.get(key)

    def register_commands(self):
        """Register all command classes with the command handler."""
        self.command_handler.register_command("add", AddCommand())
        self.command_handler.register_command("subtract", SubtractCommand())
        self.command_handler.register_command("multiply", MultiplyCommand())
        self.command_handler.register_command("divide", DivideCommand())
        self.command_handler.register_command("mean", MeanCommand())
        self.command_handler.register_command("median", MedianCommand())
        self.command_handler.register_command("standard_deviation", StandardDeviationCommand())

    def display_menu(self):
        """Display available commands in the menu."""
        print("Available Commands:")
        print("1. add                        - Add two numbers")
        print("2. subtract                   - Subtract two numbers")
        print("3. multiply                   - Multiply two numbers")
        print("4. divide                     - Divide two numbers")
        print("5. mean                       - Calculate mean of provided numbers")
        print("6. median                     - Calculate median of provided numbers")
        print("7. standard_deviation         - Calculate standard deviation of provided numbers")
        print("Type 'exit' to exit the application.")

    def handle_command_input(self, cmd_input):
        """Handle the execution of commands based on user input."""
        if cmd_input in self.command_handler.commands:
            # Command execution logic...
            return self.command_handler.execute_command(cmd_input)  # Add return here for command result

        logging.error("Unknown command: %s", cmd_input)  # Use lazy logging
        print(f"No such command: {cmd_input}")
        raise SystemExit  # Raise SystemExit when encountering an unknown command

    def get_float_input(self, prompt, is_multiple=False):
        """Get float input from the user."""
        while True:
            try:
                if is_multiple:
                    numbers = input(prompt).strip().split()
                    return [float(num) for num in numbers]  # Convert to float
            except ValueError:
                logging.error("Invalid input for numbers.")
                print("Please enter valid numbers.")

    def start(self):
        """Start the REPL for command input."""
        self.display_menu()  # Show the command menu at startup
        logging.info("Application started.")

        try:
            while True:
                cmd_input = input(">>> ").strip()
                if cmd_input.lower() == 'exit':
                    print("Exiting...")
                    logging.info("Application exit.")
                    sys.exit()  # This will raise SystemExit

                self.handle_command_input(cmd_input)

        except KeyboardInterrupt:
            logging.info("Application interrupted and exiting gracefully.")
        finally:
            logging.info("Application shutdown.")


if __name__ == "__main__":
    app = App()
    app.start()
