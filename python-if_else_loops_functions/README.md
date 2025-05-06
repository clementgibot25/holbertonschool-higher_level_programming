# Python Control Structures and Functions

This repository contains examples and explanations of fundamental Python programming concepts: functions, conditional statements (if-else), and loops.

## Table of Contents
- [Functions](#functions)
- [Conditional Statements (if-else)](#conditional-statements-if-else)
- [Loops](#loops)
  - [For Loops](#for-loops)
  - [While Loops](#while-loops)

## Functions

Functions in Python are reusable blocks of code that perform specific tasks. They help organize code and make it more maintainable.

### Key Features
- Defined using the `def` keyword
- Can accept parameters
- Can return values using the `return` statement
- Can be called multiple times

### Example
```python
def greet(name):
    return f"Hello, {name}!"

# Function call
print(greet("World"))  # Output: Hello, World!
```

## Conditional Statements (if-else)

Conditional statements allow you to execute different blocks of code based on certain conditions.

### Basic Structure
```python
if condition:
    # code to execute if condition is True
elif another_condition:
    # code to execute if previous condition was False and this condition is True
else:
    # code to execute if all previous conditions were False
```

### Comparison Operators
- `==` (equal to)
- `!=` (not equal to)
- `>` (greater than)
- `<` (less than)
- `>=` (greater than or equal to)
- `<=` (less than or equal to)

### Example
```python
age = 20

if age >= 18:
    print("You are an adult")
elif age >= 13:
    print("You are a teenager")
else:
    print("You are a child")
```

## Loops

Loops allow you to execute a block of code multiple times.

### For Loops
For loops are used when you know the number of iterations in advance.

#### Basic Structure
```python
for item in iterable:
    # code to execute for each item
```

#### Common Uses
- Iterating over lists
- Iterating over ranges
- Iterating over strings

#### Example
```python
# Iterate over a list
fruits = ["apple", "banana", "orange"]
for fruit in fruits:
    print(fruit)

# Iterate using range
for i in range(5):
    print(i)
```

### While Loops
While loops are used when you want to repeat an action as long as a condition is true.

#### Basic Structure
```python
while condition:
    # code to execute while condition is True
```

#### Important Notes
- Always ensure the condition will eventually become False to avoid infinite loops
- Use `break` to exit the loop prematurely
- Use `continue` to skip the current iteration

#### Example
```python
i = 0
while i < 5:
    print(i)
    i += 1
```

## Best Practices
1. Use meaningful function names
2. Keep functions small and focused
3. Use comments to explain complex logic
4. Follow PEP 8 style guidelines
5. Use descriptive variable names

## Contributing
Feel free to submit issues and enhancement requests!

## License
This project is licensed under the MIT License - see the LICENSE file for details.