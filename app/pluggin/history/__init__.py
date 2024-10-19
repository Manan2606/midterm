"""History Command Module

This module contains the implementation of the HistoryCommand class,
which retrieves and displays the history of executed commands.
"""
import pandas as pd
from tabulate import tabulate
from app.command import Command

class HistoryCommand(Command):
    """Command class to display history of past commands."""

    def __init__(self, history_df):
        """Initialize with a DataFrame to store the command history."""
        self.history_df = history_df

    def execute(self, *args):
        """Execute the command to display the last 10 commands."""
        if self.history_df.empty:
            return "No command history available."

        # Display the history using show_history method
        return self.show_history()

    def show_history(self):
        """Display the history of commands using tabulate for a table-like format."""
        if self.history_df.empty:
            return "No command history available."

        # Use tabulate to format the DataFrame
        return tabulate(self.history_df.values, headers=["Command"], tablefmt="fancy_grid")



    def add_to_history(self, command_str):
        """Add a new command to the history."""
        new_entry = pd.DataFrame([[command_str]], columns=["Command"])
        self.history_df = pd.concat([self.history_df, new_entry], ignore_index=True)
