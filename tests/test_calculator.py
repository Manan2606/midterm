'''test_calculator.py'''
import pytest
from app.pluggin.add import AddCommand
from app.pluggin.subtract import SubtractCommand
from app.pluggin.multiply import MultiplyCommand
from app.pluggin.divide import DivideCommand
from app.pluggin.mean import MeanCommand
from app.pluggin.median import MedianCommand
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


def test_add_command(add_command):
    """Test the add command."""
    result = add_command.execute(3, 5)
    assert result == "The result of adding 3 and 5 is equal to 8."


def test_subtract_command(subtract_command):
    """Test the subtract command."""
    result = subtract_command.execute(5, 3)
    assert result == "The result of subtracting 3 from 5 is equal to 2."


def test_subtract_negative_command(subtract_command):
    """Test the subtract negative command."""
    result = subtract_command.execute(-5, -3)
    assert result == "The result of subtracting -3 from -5 is equal to -2."


def test_subtract_command_negative_result(subtract_command):
    """Test the subtract command resulting in a negative number."""
    result = subtract_command.execute(3, 5)
    assert result == "The result of subtracting 5 from 3 is equal to -2."


def test_subtract_command_from_zero(subtract_command):
    """Test the subtract command where the result is negative."""
    result = subtract_command.execute(0, 5)
    assert result == "The result of subtracting 5 from 0 is equal to -5."


def test_multiply_command(multiply_command):
    """Test the multiply command."""
    result = multiply_command.execute(3, 5)
    assert result == "The result of multiplying 3 and 5 is equal to 15."


def test_multiply_limit_command(multiply_command):
    """Test the multiply limit command."""
    result = multiply_command.execute(3, 5)
    assert result == "The result of multiplying 3 and 5 is equal to 15."


def test_multiply_by_zero(multiply_command):
    """Test the multiply command with zero."""
    result = multiply_command.execute(5, 0)
    assert result == "The result of multiplying 5 and 0 is equal to 0."


def test_multiply_negative_numbers(multiply_command):
    """Test the multiply command with negative numbers."""
    result = multiply_command.execute(-2, -3)
    assert result == "The result of multiplying -2 and -3 is equal to 6."


def test_multiply_with_float(multiply_command):
    """Test the multiply command with float numbers."""
    result = multiply_command.execute(2.5, 4)
    assert result == "The result of multiplying 2.5 and 4 is equal to 10.0."

def test_divide_command(divide_command):
    """Test the divide command."""
    result = divide_command.execute(10, 2)
    assert result == "The result of dividing 10 by 2 is equal to 5."

    # Test division by zero
    result_zero_division = divide_command.execute(5, 0)
    assert result_zero_division == "Error: Division by zero is not allowed."


def test_mean_command(mean_command):
    """Test the mean command."""
    result = mean_command.execute(1, 2, 3)
    assert result == "The mean of 1.0, 2.0, 3.0 is 2.0."


def test_median_command(median_command):
    """Test the median command."""
    result_odd = median_command.execute(1, 2, 3)
    assert result_odd == "The median of 1.0, 2.0, 3.0 is 2.0."

    result_even = median_command.execute(1, 2, 3, 4)
    assert result_even == "The median of 1.0, 2.0, 3.0, 4.0 is 2.5."


def test_standard_deviation_command(stddev_command):
    """Test the standard deviation command."""
    result = stddev_command.execute(1, 2, 3)
    assert result.startswith("The standard deviation of 1.0, 2.0, 3.0 is")

    result = stddev_command.execute(5, 5, 5, 5)
    assert result == "The standard deviation of 5.0, 5.0, 5.0, 5.0 is 0.0."

    result = stddev_command.execute(1, 2, 3, 4, 5)
    assert result.startswith("The standard deviation of 1.0, 2.0, 3.0, 4.0, 5.0 is")
