'''test_calculator.py'''
import pytest
import pandas as pd
from app.pluggin.add import AddCommand
from app.pluggin.subtract import SubtractCommand
from app.pluggin.multiply import MultiplyCommand
from app.pluggin.divide import DivideCommand
from app.pluggin.mean import MeanCommand
from app.pluggin.median import MedianCommand
from app.pluggin.history import HistoryCommand
from app.pluggin.standard_deviation import StandardDeviationCommand

@pytest.fixture
def add_command():
    """Create an instance of the AddCommand class for testing."""
    return AddCommand()


@pytest.fixture
def subtract_command():
    """Create an instance of the SubtractCommand class for testing."""
    return SubtractCommand()


@pytest.fixture
def multiply_command():
    """Create an instance of the MultiplyCommand class for testing."""
    return MultiplyCommand()


@pytest.fixture
def divide_command():
    """Create an instance of the DivideCommand class for testing."""
    return DivideCommand()


@pytest.fixture
def mean_command():
    """Create an instance of the MeanCommand class for testing."""
    return MeanCommand()


@pytest.fixture
def median_command():
    """Create an instance of the MedianCommand class for testing."""
    return MedianCommand()


@pytest.fixture
def stddev_command():
    """Create an instance of the StandardDeviationCommand class for testing."""
    return StandardDeviationCommand()

#add command
def test_add_command(add_command):
    """Test the add command."""
    result = add_command.execute(3, 5)
    assert result == "The result of adding 3 and 5 is equal to 8."

def test_add_invalid_input(add_command):
    """Test the add command with invalid input (non-numeric)."""
    result = add_command.execute("a", 5)
    assert result == "Error: Invalid input. Please provide valid numbers."

    result = add_command.execute(3, "b")
    assert result == "Error: Invalid input. Please provide valid numbers."

    result = add_command.execute("x", "y")
    assert result == "Error: Invalid input. Please provide valid numbers."

def test_add_insufficient_arguments(add_command):
    """Test the add command with insufficient number of arguments."""
    result = add_command.execute(3)
    assert result == "Error: Please provide exactly two numbers to add."

    result = add_command.execute()
    assert result == "Error: Please provide exactly two numbers to add."

def test_add_too_many_arguments(add_command):
    """Test the add command with more than two arguments."""
    result = add_command.execute(3, 5, 7)
    assert result == "Error: Please provide exactly two numbers to add."

# subtract command
def test_subtract_command(subtract_command):
    """Test the subtract command."""
    result = subtract_command.execute(5, 3)
    assert result == "The result of subtracting 3 from 5 is equal to 2."

def test_subtract_command_invalid_input(subtract_command):
    """Test the subtract command with invalid input (non-numeric)."""
    result = subtract_command.execute("a", 5)
    assert result == "Invalid number input: 'a' or '5' is not a valid number."

    result = subtract_command.execute(3, "b")
    assert result == "Invalid number input: '3' or 'b' is not a valid number."

    result = subtract_command.execute("x", "y")
    assert result == "Invalid number input: 'x' or 'y' is not a valid number."

def test_subtract_insufficient_arguments(subtract_command):
    """Test the subtract command with insufficient number of arguments."""
    result = subtract_command.execute(5)
    assert result == "Please provide exactly two numbers to subtract."

    result = subtract_command.execute()
    assert result == "Please provide exactly two numbers to subtract."

def test_subtract_too_many_arguments(subtract_command):
    """Test the subtract command with more than two arguments."""
    result = subtract_command.execute(5, 3, 2)
    assert result == "Please provide exactly two numbers to subtract."

# multiply command
def test_multiply_command(multiply_command):
    """Test the multiply command."""
    result = multiply_command.execute(3, 5)
    assert result == "The result of multiplying 3 and 5 is equal to 15."

def test_multiply_invalid_input(multiply_command):
    """Test the multiply command with invalid input (non-numeric)."""
    result = multiply_command.execute("a", 5)
    assert result == "Invalid number input: 'a' or '5' is not a valid number."

    result = multiply_command.execute(3, "b")
    assert result == "Invalid number input: '3' or 'b' is not a valid number."

    result = multiply_command.execute("x", "y")
    assert result == "Invalid number input: 'x' or 'y' is not a valid number."

def test_multiply_insufficient_arguments(multiply_command):
    """Test the multiply command with insufficient number of arguments."""
    result = multiply_command.execute(3)
    assert result == "Please provide exactly two numbers to multiply."

    result = multiply_command.execute()
    assert result == "Please provide exactly two numbers to multiply."

def test_multiply_too_many_arguments(multiply_command):
    """Test the multiply command with more than two arguments."""
    result = multiply_command.execute(3, 5, 7)
    assert result == "Please provide exactly two numbers to multiply."

# divide command
def test_divide_command(divide_command):
    """Test the divide command."""
    result = divide_command.execute(10, 2)
    assert result == "The result of dividing 10 by 2 is equal to 5."
    # Test division by zero
    result_zero_division = divide_command.execute(5, 0)
    assert result_zero_division == "Error: Division by zero is not allowed."

def test_divide_negative_numbers(divide_command):
    """Test the divide command with negative numbers."""
    result = divide_command.execute(-10, 2)
    assert result == "The result of dividing -10 by 2 is equal to -5."

    result = divide_command.execute(10, -2)
    assert result == "The result of dividing 10 by -2 is equal to -5."

    result = divide_command.execute(-10, -2)
    assert result == "The result of dividing -10 by -2 is equal to 5."

def test_divide_invalid_input(divide_command):
    """Test the divide command with invalid input (non-numeric)."""
    result = divide_command.execute("a", 5)
    assert result == "Invalid number input: 'a' or '5' is not a valid number."

    result = divide_command.execute(3, "b")
    assert result == "Invalid number input: '3' or 'b' is not a valid number."

    result = divide_command.execute("x", "y")
    assert result == "Invalid number input: 'x' or 'y' is not a valid number."

def test_divide_insufficient_arguments(divide_command):
    """Test the divide command with insufficient number of arguments."""
    result = divide_command.execute(3)
    assert result == "Please provide exactly two numbers to divide."

    result = divide_command.execute()
    assert result == "Please provide exactly two numbers to divide."

def test_divide_too_many_arguments(divide_command):
    """Test the divide command with more than two arguments."""
    result = divide_command.execute(3, 5, 7)
    assert result == "Please provide exactly two numbers to divide."

def test_divide_by_zero(divide_command):
    """Test the divide command where the divisor is zero."""
    result = divide_command.execute(5, 0)
    assert result == "Error: Division by zero is not allowed."

# mean command
def test_mean_command(mean_command):
    """Test the mean command."""
    result = mean_command.execute(1, 2, 3)
    assert result == "The mean of 1.0, 2.0, 3.0 is 2.0."

def test_mean_command_with_no_input(mean_command):
    """Test the mean command with no input."""
    result = mean_command.execute()
    assert result == "Please provide at least one number to calculate the mean."

# median command
def test_median_command(median_command):
    """Test the median command."""
    result_odd = median_command.execute(1, 2, 3)
    assert result_odd == "The median of 1.0, 2.0, 3.0 is 2.0."

    result_even = median_command.execute(1, 2, 3, 4)
    assert result_even == "The median of 1.0, 2.0, 3.0, 4.0 is 2.5."

# median
def test_median_command_with_no_input(median_command):
    """Test the median command with no input."""
    result = median_command.execute()
    assert result == "Please provide at least one number to calculate the median."

# SD
def test_standard_deviation_command(stddev_command):
    """Test the standard deviation command."""
    result = stddev_command.execute(1, 2, 3)
    assert result.startswith("The standard deviation of 1.0, 2.0, 3.0 is")

    result = stddev_command.execute(5, 5, 5, 5)
    assert result == "The standard deviation of 5.0, 5.0, 5.0, 5.0 is 0.0."

    result = stddev_command.execute(1, 2, 3, 4, 5)
    assert result.startswith("The standard deviation of 1.0, 2.0, 3.0, 4.0, 5.0 is")

def test_stddev_command_with_no_input(stddev_command):
    """Test the standard deviation command with no input."""
    result = stddev_command.execute()
    assert result == "Please provide at least one number to calculate the standard deviation."


@pytest.fixture
def history_command():
    """Fixture to create an instance of HistoryCommand for testing."""
    history_df = pd.DataFrame(columns=["Command"])
    return HistoryCommand(history_df)

def test_empty_history(history_command):
    """Test the case when no command history is available."""
    result = history_command.execute()
    assert result == "No command history available."

def test_add_to_history(history_command):
    """Test adding a command to history."""
    history_command.add_to_history("add 2 3")
    assert history_command.history_df.iloc[0]["Command"] == "add 2 3"
    assert len(history_command.history_df) == 1

def test_show_history(history_command):
    """Test displaying the history of commands."""
    history_command.add_to_history("add 2 3")
    history_command.add_to_history("subtract 5 2")
    result = history_command.show_history()
    assert "add 2 3" in result
    assert "subtract 5 2" in result

def test_multiple_commands(history_command):
    """Test adding multiple commands to history."""
    commands = ["multiply 3 4", "divide 8 2", "mean 1 2 3 4 5"]
    for command in commands:
        history_command.add_to_history(command)

    result = history_command.show_history()
    for command in commands:
        assert command in result

def test_show_history_with_empty_command(history_command):
    """Test showing history after adding an empty command."""
    history_command.add_to_history("")
    result = history_command.show_history()
    assert "No command history available." not in result
    assert "" in result  # Check that empty command is stored
