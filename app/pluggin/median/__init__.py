"""Median Command Module

This module contains the implementation of the MedianCommand class,
which calculates the median of a given set of numbers.
"""

from statistics import median
from app.command import Command

class MedianCommand(Command):
    """Command class to calculate the median of a set of numbers."""

    def execute(self, *args):
        if not args:
            return "Please provide at least one number to calculate the median."

        numbers = [float(num) for num in args]  # Convert arguments to float
        formatted_numbers = ', '.join(f'{num:.1f}' for num in numbers)  # Format numbers to one decimal place
        return f"The median of {formatted_numbers} is {median(numbers):.1f}."  # Correctly formats to one decimal
