# MidTerm Project: Advanced Python Calculator

## Advanced Python-Based Calculator Application

### Table of Contents
- [Overview](#overview)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Commands](#commands)
- [Design Patterns](#design-patterns)
- [Environment Variables](#environment-variables)
- [Logging](#logging)
- [Error Handling](#error-handling)
- [Testing](#testing)
- [Contributing](#contributing)
- [Video Demonstration](#video-demonstration)

### Overview
This project is an advanced calculator application developed in Python. It supports various mathematical operations and includes features such as command history management, dynamic plugin architecture, and data analysis capabilities using the Pandas library. The application provides a user-friendly REPL (Read-Eval-Print Loop) interface for interactive calculations.

### Features
- **Basic Operations**: Perform addition, subtraction, multiplication, and division.
- **Statistical Functions**: Calculate mean, median, and standard deviation.
- **History Management**: Track and display the history of executed commands.
- **Dynamic Plugins**: Utilize an extensible architecture for adding new commands seamlessly.
- **Data Handling**: Leverage the Pandas library for effective command history management and analysis.
- **Comprehensive Testing**: Implement unit tests to ensure functionality and reliability.

### Design Patterns
This application utilizes several design patterns to enhance modularity and maintainability:
- **Command Pattern**: Encapsulates command requests as objects, allowing for parameterization and queuing of requests, while supporting undoable operations.
- **Strategy Pattern**: Implements a family of algorithms (arithmetic operations) and makes them interchangeable within the command structure.
- **Facade Pattern**: Simplifies interactions with complex subsystems (like command handling and history management) through a unified interface.

## Design Patterns Documentation
For a detailed explanation of the design patterns used in this project, including their rationale and implementation details, please refer to the [Design Patterns Documentation](./design_patterns_documentation.md).

### Environment Variables
The application uses environment variables to configure settings. The `load_environment_variables` method loads these variables, ensuring that sensitive information remains secure. For details, see [this method](app/__init__.py).

### Logging
Logging is implemented to track application behavior and errors. The `configure_logging` method sets up logging configurations. See the implementation [here](app/__init__.py).

### Error Handling
The application employs error handling strategies, including try/catch blocks to manage exceptions effectively. This implementation follows the principles of "Look Before You Leap" (LBYL) and "Easier to Ask for Forgiveness than Permission" (EAFP). For more information, refer to [this section](app/__init__.py).

### Installation
To set up the Advanced Python Calculator application, follow these steps:

1. **Clone the Repository**: Start by cloning the repository from GitHub to your local machine. Replace `<repository-url>` with the URL of your GitHub repository.
   ```bash
   git clone <repository-url>
   cd <repository-directory>

2. Install Dependencies : Once inside the project directory, install the required packages using pip. Make sure you have a requirements.txt file in your repository, which lists all the necessary dependencies.
    
    pip install -r requirements.txt

### Usage

1. Run the application:
    python3 main.py
2. Follow the prompts to enter commands in the REPL interface.
3. Type exit to close the application.

### Commands

Basic Arithmetic: add <num1> <num2>, subtract <num1> <num2>, multiply <num1> <num2>, divide <num1> <num2>

Statistical Calculations: mean <num1> <num2> ..., median <num1> <num2> ..., standard_deviation <num1> <num2> ...

History Management: history (view command history), clear history (clear command history)

### Testing

To run the tests, execute the following commands:

pytest

pytest --pylint

pytest --pylint --cov

### Contributing

Contributions are welcome! Please feel free to submit a pull request or open an issue for any bugs or feature requests.

### Video Demonstration

[Watch the video demonstration here](https://youtu.be/Rywg-xe0w9o)
