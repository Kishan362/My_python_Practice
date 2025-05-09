# Python Practice

This repository contains various Python scripts demonstrating fundamental programming concepts and Python features.

## Files Overview

### 1. `Augmented_assignment_oprator.py`

Demonstrates augmented assignment operators in Python (+=, -=, etc.) which provide a shorter way to update variables with operations.

### 2. `Data_types_0.py`

An overview of Python's basic data types including:

- Integers
- Floats
- Booleans
- Strings
- Lists
- Tuples
- Dictionaries
- Sets
- Classes and specialized data types

### 3. `Expressions_and_statments.py`

Explains the difference between expressions (code that produces a value) and statements (complete lines of code) in Python.

### 4. `Numbers0.py`

Covers fundamental operations with numbers in Python:

- Basic arithmetic operations (+, -, \*, /, \*\*, //, %)
- Type checking with `type()`
- Math functions like `round()` and `abs()`
- Binary conversion with `bin()`

### 5. `numbers1(BIN and Complex).py`

Explores more advanced number concepts:

- Complex numbers and operations
- Binary number representation
- Converting between binary and decimal

### 6. `Oprator_precedence.py`

Demonstrates the order of operations (operator precedence) in Python with examples showing how different expressions are evaluated.

### 7. `strings_.py`

Covers string basics in Python:

- String creation with single and double quotes
- Multi-line strings with triple quotes
- String concatenation
- String variables

### 8. `variables_.py`

Explains Python variables:

- Variable naming conventions and rules
- Snake case naming
- Constants
- Multiple variable assignment
- Dunder methods

## Getting Started

To run any of these scripts, use Python 3:

```bash
python script_name.py
```

For example:

```bash
python Numbers0.py
```

## Prerequisites

- Python 3.x installed on your system

## Python Developer Fundamentals

### 1. PEP 8 - Style Guide for Python Code

PEP 8 is Python's style guide. Following these conventions makes your code more readable and maintainable.

#### Indentation

Use 4 spaces per indentation level (not tabs).

```python
# Good
def function():
    if True:
        print("Properly indented")

# Bad
def function():
  if True:
      print("Inconsistent indentation")
```

#### Maximum Line Length

Limit lines to 79 characters.

```python
# Good
long_string = ("This is a properly wrapped long string that "
               "follows the PEP 8 guidelines for line length")

# Bad
long_string = "This is a very long string that exceeds the recommended line length and makes code harder to read"
```

#### Imports

Imports should be on separate lines and grouped in the following order:

1. Standard library imports
2. Related third-party imports
3. Local application/library specific imports

```python
# Good
import os
import sys

from flask import Flask
from sqlalchemy import Column

from myproject.models import User
```

### 2. Variable Naming Conventions

#### Snake Case for Variables and Functions

```python
user_name = "John"
first_number = 42

def calculate_average(numbers):
    return sum(numbers) / len(numbers)
```

#### Pascal Case for Classes

```python
class UserAccount:
    def __init__(self, username, email):
        self.username = username
        self.email = email
```

#### Uppercase with Underscores for Constants

```python
PI = 3.14159
MAX_CONNECTIONS = 100
DEFAULT_TIMEOUT = 60
```

### 3. Data Structures and Their Use Cases

#### Lists

Ordered, mutable collections of items.

```python
# Creating a list
fruits = ["apple", "banana", "cherry"]

# Adding items
fruits.append("orange")  # ["apple", "banana", "cherry", "orange"]

# Accessing items
first_fruit = fruits[0]  # "apple"

# Slicing
first_two = fruits[0:2]  # ["apple", "banana"]

# List comprehension
squared = [x**2 for x in range(5)]  # [0, 1, 4, 9, 16]
```

#### Dictionaries

Key-value pairs for fast lookups.

```python
# Creating a dictionary
user = {"name": "John", "age": 30, "city": "New York"}

# Accessing values
user_name = user["name"]  # "John"

# Adding/updating entries
user["email"] = "john@example.com"

# Dictionary comprehension
squared_dict = {x: x**2 for x in range(5)}  # {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}
```

#### Sets

Unordered collections of unique items.

```python
# Creating a set
unique_numbers = {1, 2, 3, 3, 4, 4, 5}  # {1, 2, 3, 4, 5}

# Adding items
unique_numbers.add(6)  # {1, 2, 3, 4, 5, 6}

# Set operations
set_a = {1, 2, 3}
set_b = {3, 4, 5}
union = set_a | set_b  # {1, 2, 3, 4, 5}
intersection = set_a & set_b  # {3}
difference = set_a - set_b  # {1, 2}
```

#### Tuples

Immutable ordered collections.

```python
# Creating a tuple
coordinates = (10, 20)

# Tuple unpacking
x, y = coordinates  # x = 10, y = 20

# Tuples as dictionary keys (since they're immutable)
locations = {(35.6895, 139.6917): "Tokyo", (40.7128, 74.0060): "New York"}
```

### 4. Functions and Parameters

#### Default Parameters

```python
def greet(name, greeting="Hello"):
    return f"{greeting}, {name}!"

greet("Alice")  # "Hello, Alice!"
greet("Bob", "Hi")  # "Hi, Bob!"
```

#### \*args and \*\*kwargs

```python
# *args for variable positional arguments
def sum_all(*args):
    return sum(args)

sum_all(1, 2, 3, 4)  # 10

# **kwargs for variable keyword arguments
def user_info(**kwargs):
    return kwargs

user_info(name="Alice", age=30, city="Boston")  # {'name': 'Alice', 'age': 30, 'city': 'Boston'}
```

#### Type Hints (Python 3.5+)

```python
def calculate_area(width: float, height: float) -> float:
    return width * height

# With default values
def greet(name: str, greeting: str = "Hello") -> str:
    return f"{greeting}, {name}!"
```

### 5. Error Handling

#### Try-Except Blocks

```python
try:
    result = 10 / 0
except ZeroDivisionError:
    result = 0
    print("Cannot divide by zero")
finally:
    print("Operation completed")
```

#### Raising Exceptions

```python
def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b

try:
    divide(10, 0)
except ValueError as e:
    print(e)  # "Cannot divide by zero"
```

#### Custom Exceptions

```python
class InsufficientFundsError(Exception):
    pass

def withdraw(balance, amount):
    if amount > balance:
        raise InsufficientFundsError("Not enough funds")
    return balance - amount
```

### 6. Object-Oriented Programming

#### Class Definition

```python
class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_description(self):
        return f"{self.year} {self.make} {self.model}"

    def update_odometer(self, mileage):
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")
```

#### Inheritance

```python
class ElectricCar(Car):
    def __init__(self, make, model, year, battery_size):
        super().__init__(make, model, year)
        self.battery_size = battery_size

    def describe_battery(self):
        return f"This car has a {self.battery_size}-kWh battery."
```

#### Properties and Decorators

```python
class Temperature:
    def __init__(self, celsius=0):
        self._celsius = celsius

    @property
    def celsius(self):
        return self._celsius

    @celsius.setter
    def celsius(self, value):
        if value < -273.15:
            raise ValueError("Temperature below absolute zero is not possible")
        self._celsius = value

    @property
    def fahrenheit(self):
        return (self.celsius * 9/5) + 32

    @fahrenheit.setter
    def fahrenheit(self, value):
        self.celsius = (value - 32) * 5/9
```

### 7. Modules and Packages

#### Creating a Module

```python
# math_operations.py
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

PI = 3.14159
```

#### Importing a Module

```python
# Option 1: Import the module
import math_operations
result = math_operations.add(5, 3)  # 8

# Option 2: Import specific functions
from math_operations import add, subtract
result = add(5, 3)  # 8

# Option 3: Import with alias
import math_operations as math
result = math.add(5, 3)  # 8
```

#### Creating a Package

```
my_package/
├── __init__.py
├── module1.py
└── module2.py
```

### 8. File Operations

#### Reading Files

```python
# Reading an entire file
with open('file.txt', 'r') as file:
    content = file.read()

# Reading line by line
with open('file.txt', 'r') as file:
    for line in file:
        print(line.strip())
```

#### Writing Files

```python
# Writing to a file
with open('output.txt', 'w') as file:
    file.write("Hello, World!")

# Appending to a file
with open('output.txt', 'a') as file:
    file.write("\nAppended line")
```

### 9. List Comprehensions and Generator Expressions

#### List Comprehensions

```python
# Traditional way
squares = []
for i in range(10):
    squares.append(i**2)

# List comprehension
squares = [i**2 for i in range(10)]

# With conditional
even_squares = [i**2 for i in range(10) if i % 2 == 0]
```

#### Generator Expressions

```python
# Generator expression (memory efficient)
sum_of_squares = sum(i**2 for i in range(10000))

# Reading large files efficiently
with open('large_file.txt', 'r') as file:
    line_count = sum(1 for line in file)
```

### 10. Context Managers

#### Using with Statement

```python
# File operations
with open('file.txt', 'r') as file:
    content = file.read()
# File is automatically closed after the block

# Database connections
with connection.cursor() as cursor:
    cursor.execute("SELECT * FROM users")
    results = cursor.fetchall()
# Cursor is automatically closed
```

#### Creating Custom Context Managers

```python
from contextlib import contextmanager

@contextmanager
def timer():
    import time
    start = time.time()
    yield
    end = time.time()
    print(f"Elapsed time: {end - start:.2f} seconds")

# Usage
with timer():
    # Code to be timed
    result = sum(i**2 for i in range(1000000))
```

### 11. Decorators

#### Basic Decorator

```python
def log_function_call(func):
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__} with args: {args}, kwargs: {kwargs}")
        result = func(*args, **kwargs)
        print(f"{func.__name__} returned: {result}")
        return result
    return wrapper

@log_function_call
def add(a, b):
    return a + b

add(3, 5)  # Logs the function call and returns 8
```

#### Decorator with Arguments

```python
def repeat(n):
    def decorator(func):
        def wrapper(*args, **kwargs):
            result = None
            for _ in range(n):
                result = func(*args, **kwargs)
            return result
        return wrapper
    return decorator

@repeat(3)
def greet(name):
    print(f"Hello, {name}!")

greet("Alice")  # Prints "Hello, Alice!" three times
```

### 12. Virtual Environments

Virtual environments allow you to create isolated Python environments for different projects.

```bash
# Creating a virtual environment
python -m venv myenv

# Activating the virtual environment
# On Windows
myenv\Scripts\activate
# On macOS/Linux
source myenv/bin/activate

# Installing packages
pip install package_name

# Saving dependencies
pip freeze > requirements.txt

# Installing from requirements
pip install -r requirements.txt

# Deactivating
deactivate
```

### 13. Testing

#### Unit Testing with unittest

```python
import unittest

def add(a, b):
    return a + b

class TestAddFunction(unittest.TestCase):
    def test_add_positive_numbers(self):
        self.assertEqual(add(2, 3), 5)

    def test_add_negative_numbers(self):
        self.assertEqual(add(-1, -1), -2)

    def test_add_mixed_numbers(self):
        self.assertEqual(add(-1, 1), 0)

if __name__ == '__main__':
    unittest.main()
```

#### Testing with pytest

```python
# test_functions.py
def add(a, b):
    return a + b

def test_add_positive_numbers():
    assert add(2, 3) == 5

def test_add_negative_numbers():
    assert add(-1, -1) == -2

def test_add_mixed_numbers():
    assert add(-1, 1) == 0
```

### 14. Debugging

#### Using print statements

```python
def complex_calculation(a, b, c):
    print(f"Inputs: a={a}, b={b}, c={c}")

    intermediate = a * b
    print(f"Intermediate result: {intermediate}")

    final_result = intermediate / c
    print(f"Final result: {final_result}")

    return final_result
```

#### Using the debugger (pdb)

```python
def complex_calculation(a, b, c):
    import pdb; pdb.set_trace()  # Debugger will pause here
    intermediate = a * b
    final_result = intermediate / c
    return final_result

# In Python 3.7+, you can use breakpoint() instead
def complex_calculation(a, b, c):
    breakpoint()  # Debugger will pause here
    intermediate = a * b
    final_result = intermediate / c
    return final_result
```

### 15. Performance Optimization

#### Profiling Code

```python
import cProfile

def slow_function():
    result = 0
    for i in range(1000000):
        result += i
    return result

cProfile.run('slow_function()')
```

#### Timing Code

```python
import time

start_time = time.time()
result = slow_function()
end_time = time.time()

print(f"Function took {end_time - start_time:.4f} seconds to run")
```

### 16. Asynchronous Programming (Python 3.5+)

#### Basic Async/Await

```python
import asyncio

async def fetch_data():
    print("Start fetching")
    await asyncio.sleep(2)  # Simulating an I/O operation
    print("Done fetching")
    return {"data": 100}

async def process_data():
    print("Start processing")
    await asyncio.sleep(1)  # Simulating an I/O operation
    print("Done processing")
    return {"result": 200}

async def main():
    data_task = asyncio.create_task(fetch_data())
    process_task = asyncio.create_task(process_data())

    data = await data_task
    processed = await process_task

    print(f"Final result: {data['data'] + processed['result']}")

# Python 3.7+
asyncio.run(main())
```

### 17. Type Checking with mypy

```python
# example.py
def greet(name: str) -> str:
    return f"Hello, {name}!"

# This will cause a type error when checked with mypy
result = greet(42)  # Passing an int instead of a str

# Run mypy with: mypy example.py
```

### 18. Functional Programming

#### Lambda Functions

```python
# Traditional function
def add(a, b):
    return a + b

# Lambda equivalent
add = lambda a, b: a + b

# Used with higher-order functions
numbers = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x**2, numbers))  # [1, 4, 9, 16, 25]
```

#### Map, Filter, Reduce

```python
from functools import reduce

numbers = [1, 2, 3, 4, 5]

# Map: Apply a function to each item
squared = list(map(lambda x: x**2, numbers))  # [1, 4, 9, 16, 25]

# Filter: Keep items that satisfy a condition
evens = list(filter(lambda x: x % 2 == 0, numbers))  # [2, 4]

# Reduce: Cumulatively apply a function to items
sum_all = reduce(lambda x, y: x + y, numbers)  # 15
```

### 19. Regular Expressions

```python
import re

# Matching patterns
text = "Contact us at info@example.com or support@example.org"
emails = re.findall(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b', text)
# ['info@example.com', 'support@example.org']

# Replacing patterns
censored = re.sub(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b', '[EMAIL REDACTED]', text)
# "Contact us at [EMAIL REDACTED] or [EMAIL REDACTED]"

# Validating input
def is_valid_email(email):
    pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    return bool(re.match(pattern, email))

is_valid_email("user@example.com")  # True
is_valid_email("invalid-email")  # False
```

### 20. Documentation

#### Docstrings

```python
def calculate_area(width, height):
    """
    Calculate the area of a rectangle.

    Args:
        width (float): The width of the rectangle.
        height (float): The height of the rectangle.

    Returns:
        float: The area of the rectangle.

    Raises:
        ValueError: If width or height is negative.
    """
    if width < 0 or height < 0:
        raise ValueError("Width and height must be non-negative")
    return width * height
```

#### Type Hints with Documentation

```python
def calculate_area(width: float, height: float) -> float:
    """
    Calculate the area of a rectangle.

    Args:
        width: The width of the rectangle.
        height: The height of the rectangle.

    Returns:
        The area of the rectangle.

    Raises:
        ValueError: If width or height is negative.
    """
    if width < 0 or height < 0:
        raise ValueError("Width and height must be non-negative")
    return width * height
```
