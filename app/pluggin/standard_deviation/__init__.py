"""Standard Deviation Command Module

This module contains the implementation of the StandardDeviationCommand class,
which calculates the standard deviation of a given set of numbers.
"""

from statistics import stdev
from app.command import Command

class StandardDeviationCommand(Command):
    """Command class to calculate the standard deviation of a set of numbers."""

    def execute(self, *args):
        if not args:
            return "Please provide at least one number to calculate the standard deviation."

        numbers = [float(num) for num in args]  # Convert arguments to float
        return f"The standard deviation of {', '.join(map(str, numbers))} is {stdev(numbers)}."
