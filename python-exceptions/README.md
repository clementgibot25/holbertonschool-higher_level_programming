# Exception Handling in Python

## What’s the Difference Between Errors and Exceptions
- **Errors** are problems in a program that cause it to crash. Some errors are not meant to be handled by programs (e.g., syntax errors).
- **Exceptions** are specific types of errors that can be detected and handled during execution, allowing the program to recover or exit gracefully.

## What are Exceptions and How to Use Them
An **exception** is an event that disrupts the normal flow of a program when an error occurs. In Python, exceptions can be caught and handled using `try` and `except` blocks.

**Example:**
```python
try:
    result = 10 / 0
except ZeroDivisionError:
    print("Cannot divide by zero")
```

## When Do We Need to Use Exceptions
- When you expect that an operation might fail (e.g., file operations, user input, network requests).
- When you want to handle errors gracefully and avoid program crashes.

## How to Correctly Handle an Exception
Use `try`/`except` to catch exceptions and handle them appropriately:
```python
def safe_divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        print("Cannot divide by zero")
        return None
    except TypeError:
        print("Invalid types for division")
        return None
```

## What’s the Purpose of Catching Exceptions
- To prevent the program from crashing unexpectedly.
- To provide meaningful error messages to the user.
- To allow the program to recover or take alternative actions when an error occurs.

## How to Raise a Builtin Exception
You can raise an exception intentionally using the `raise` keyword:
```python
def check_positive(number):
    if number < 0:
        raise ValueError("Number must be positive")
    return number
```

## When Do We Need to Implement a Clean-Up Action After an Exception
Sometimes, you need to ensure that resources are released or certain actions are taken, even if an exception occurs. Use the `finally` block for clean-up actions:
```python
try:
    file = open('data.txt', 'r')
    # process file
except FileNotFoundError:
    print("File not found")
finally:
    if 'file' in locals():
        file.close()  # This runs whether or not an exception occurred
```

## Summary
- Errors and exceptions are not the same; exceptions can be handled.
- Use exceptions to handle expected and unexpected problems in your code.
- Always clean up resources (like files or network connections) using `finally` or context managers.

## What are Exceptions and How to Use Them
An **exception** is an error that occurs during program execution. Python uses exceptions to handle errors gracefully.

**Example:**
```python
def divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        print("Cannot divide by zero")
        return None
```

## Common Exception Types
- `ZeroDivisionError`: Division by zero.
- `IndexError`: Accessing an index out of range.
- `KeyError`: Accessing a dictionary key that doesn't exist.
- `ValueError`: Invalid value for a function argument.
- `TypeError`: Invalid type for an operation.

## How to Handle Exceptions
```python
def safe_divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        print("Cannot divide by zero")
        return None
    except TypeError:
        print("Invalid types for division")
        return None
```
