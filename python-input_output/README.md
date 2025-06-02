# Python Input/Output and More

This document covers fundamental concepts in Python, focusing on input/output operations, JSON handling, and command-line arguments.

## Table of Contents
1. [Why Python Programming is Awesome](#why-python-programming-is-awesome)
2. [File Handling in Python](#file-handling-in-python)
   - [Opening a File](#opening-a-file)
   - [Writing Text to a File](#writing-text-to-a-file)
   - [Reading File Content](#reading-file-content)
   - [Moving the Cursor](#moving-the-cursor)
   - [Ensuring a File is Closed](#ensuring-a-file-is-closed)
   - [The `with` Statement](#the-with-statement)
3. [Working with JSON](#working-with-json)
   - [What is JSON?](#what-is-json)
   - [Serialization and Deserialization](#serialization-and-deserialization)
   - [Python to JSON (Serialization)](#python-to-json-serialization)
   - [JSON to Python (Deserialization)](#json-to-python-deserialization)
4. [Command Line Arguments](#command-line-arguments)

## Why Python Programming is Awesome

Python is a versatile, high-level programming language known for its readability and simplicity. Here are a few reasons why it's awesome:

- **Easy to Learn and Use:** Python has a clean syntax that is easy to pick up, making it ideal for beginners and experienced programmers alike.
- **Extensive Standard Library:** It comes with a large standard library that provides tools for a wide range of tasks, from web development to data science.
- **Cross-Platform Compatibility:** Python code can run on various operating systems like Windows, macOS, and Linux without modification.
- **Strong Community Support:** A vast and active community contributes to a wealth of libraries, frameworks, and resources.
- **Versatility:** Python is used in web development (Django, Flask), data analysis (Pandas, NumPy), machine learning (TensorFlow, Scikit-learn), automation, scripting, and much more.
- **Interpreted Language:** This allows for rapid prototyping and testing as code is executed line by line.

## File Handling in Python

Python provides built-in functions to create, read, and write files.

### Opening a File

The `open()` function is used to open a file. It returns a file object, also called a handle, as it is used to read or modify the file accordingly.

```python
# Syntax: open(filename, mode)

# Modes:
# 'r' - Read (default). Throws an error if the file does not exist.
# 'w' - Write. Creates a new file if it does not exist or truncates the file if it exists.
# 'a' - Append. Creates a new file if it does not exist or appends to the end of the file if it exists.
# 'x' - Exclusive creation. Creates a new file, but fails if the file already exists.
# 'b' - Binary mode (e.g., 'rb', 'wb'). For handling binary files like images.
# 't' - Text mode (default).
# '+' - Open for updating (reading and writing, e.g., 'r+', 'w+').

# Example: Opening a file for reading
# f = open("example.txt", "r")

# Example: Opening a file for writing
# f_write = open("output.txt", "w")
```

### Writing Text to a File

Once a file is opened in write (`'w'`) or append (`'a'`) mode, you can write content to it using the `write()` or `writelines()` methods.

```python
# Open a file for writing (will create or overwrite)
with open("output.txt", "w") as f:
    f.write("Hello, Python!\n")
    f.write("This is a new line.\n")

# Open a file for appending
with open("output.txt", "a") as f:
    lines = ["Appending a line.\n", "Another appended line.\n"]
    f.writelines(lines)
```
**Note:** `write()` expects a string. `writelines()` expects an iterable of strings.

### Reading File Content

There are several ways to read content from a file opened in read mode (`'r'`):

1.  **Reading the Full Content (`read()`)**
    Reads the entire content of the file into a single string.
    ```python
    with open("example.txt", "r") as f:
        content = f.read()
        print(content)
    ```

2.  **Reading Line by Line**
    -   **`readline()`**: Reads a single line from the file, including the newline character at the end. Returns an empty string at the end of the file.
        ```python
        with open("example.txt", "r") as f:
            line1 = f.readline()
            print(f"First line: {line1.strip()}")
            line2 = f.readline()
            print(f"Second line: {line2.strip()}")
        ```
    -   **`readlines()`**: Reads all lines from the file and returns them as a list of strings, where each string is a line including the newline character.
        ```python
        with open("example.txt", "r") as f:
            all_lines = f.readlines()
            for line in all_lines:
                print(line.strip())
        ```
    -   **Iterating over the file object**: This is the most memory-efficient way to read a file line by line.
        ```python
        with open("example.txt", "r") as f:
            for line in f:
                print(line.strip()) # .strip() removes leading/trailing whitespace, including newline
        ```

### Moving the Cursor

File objects have a cursor that indicates the current position for reading or writing.

-   **`tell()`**: Returns the current position of the cursor (in bytes from the beginning of the file).
-   **`seek(offset, whence=0)`**: Changes the current file position.
    -   `offset`: Number of bytes to move.
    -   `whence`: Reference point for the offset.
        -   `0` (default): Absolute file positioning (from the beginning of the file).
        -   `1`: Seek relative to the current position.
        -   `2`: Seek relative to the file's end.

```python
with open("example.txt", "r") as f:
    print(f"Initial cursor position: {f.tell()}") # Output: 0
    line = f.readline()
    print(f"Cursor after reading one line: {f.tell()}")
    
    f.seek(0) # Go back to the beginning of the file
    print(f"Cursor after seek(0): {f.tell()}") # Output: 0
    content_from_start = f.read(5) # Read first 5 bytes
    print(f"Content: '{content_from_start}'")
```
**Note:** `seek()` and `tell()` work with bytes. In text mode, the exact byte position of characters can be tricky due to encoding. It's generally safer to `seek(0)` or use offsets obtained from `tell()` earlier.

### Ensuring a File is Closed

It's crucial to close a file after you're done with it to free up system resources and ensure that all data is written (flushed) to the disk.

1.  **Manual `close()`**
    ```python
    f = open("example.txt", "r")
    try:
        # Perform file operations
        content = f.read()
        print(content)
    finally:
        f.close() # Ensures file is closed even if errors occur
    ```

2.  **The `with` Statement (Recommended)**
    The `with` statement provides a cleaner way to manage resources like file objects. It automatically closes the file when the block is exited, even if errors occur.

### The `with` Statement

The `with` statement simplifies exception handling by encapsulating common preparation and cleanup tasks in so-called context managers. When a file is opened using `with`, it is automatically closed upon exiting the `with` block.

```python
with open("example.txt", "r") as f:
    content = f.read()
    print("File content read using 'with':")
    print(content)
# File 'f' is automatically closed here, even if an error occurred inside the 'with' block.

# Example with writing:
with open("new_file.txt", "w") as f_new:
    f_new.write("This file was created using 'with'.")
# f_new is automatically closed.
```
This is the preferred way to handle files in Python due to its conciseness and safety.

## Working with JSON

JSON (JavaScript Object Notation) is a lightweight data-interchange format. It is easy for humans to read and write and easy for machines to parse and generate.

### What is JSON?
-   A text format that is completely language independent.
-   Uses human-readable text to transmit data objects consisting of attribute–value pairs and array data types (or any other serializable value).
-   Commonly used for transmitting data in web applications (e.g., sending some data from the server to the client, so it can be displayed on a web page, or vice versa).

**JSON supports the following data types:**
-   **String:** Enclosed in double quotes (e.g., `"hello"`).
-   **Number:** Integer or floating-point (e.g., `101`, `3.14`).
-   **Boolean:** `true` or `false`.
-   **Array:** Ordered list of values, enclosed in square brackets (e.g., `[1, "apple", true]`).
-   **Object:** Unordered collection of key/value pairs, enclosed in curly braces. Keys must be strings (e.g., `{"name": "John", "age": 30}`).
-   **Null:** Represented as `null`.

### Serialization and Deserialization

-   **Serialization:** The process of converting a Python data structure (e.g., a dictionary or list) into a JSON formatted string. This is often done when you want to store data or send it over a network.
-   **Deserialization:** The process of converting a JSON formatted string back into a Python data structure.

Python's `json` module is used for these operations.

```python
import json
```

### Python to JSON (Serialization)

The `json.dumps()` method is used to serialize a Python object into a JSON string.

```python
import json

python_dict = {
    "name": "Alice",
    "age": 25,
    "isStudent": True,
    "courses": [
        {"title": "Math", "credits": 3},
        {"title": "History", "credits": 3}
    ],
    "address": None
}

# Convert Python dictionary to JSON string
json_string = json.dumps(python_dict, indent=4) # indent for pretty printing

print("JSON String:")
print(json_string)

# To write to a file, use json.dump() (without 's')
with open("data.json", "w") as f_json:
    json.dump(python_dict, f_json, indent=4)
```

### JSON to Python (Deserialization)

The `json.loads()` method is used to deserialize a JSON string into a Python object.

```python
import json

json_data_string = '''
{
    "name": "Bob",
    "age": 30,
    "city": "New York",
    "hobbies": ["reading", "hiking"]
}
'''

# Convert JSON string to Python dictionary
python_obj = json.loads(json_data_string)

print("\nPython Dictionary:")
print(python_obj)
print(f"Name: {python_obj['name']}")
print(f"First hobby: {python_obj['hobbies'][0]}")

# To read from a JSON file, use json.load() (without 's')
# Assuming 'data.json' exists from the previous example
with open("data.json", "r") as f_json_read:
    loaded_python_obj = json.load(f_json_read)
    print("\nLoaded from data.json:")
    print(loaded_python_obj)
```

## Command Line Arguments

Python scripts can accept arguments passed to them from the command line. The `sys` module provides access to these arguments.

-   `sys.argv`: This is a list in Python, which contains the command-line arguments passed to the script.
    -   `sys.argv[0]` is the name of the script itself.
    -   `sys.argv[1]` is the first argument, `sys.argv[2]` is the second, and so on.

```python
# Save this as script_name.py
import sys

if __name__ == "__main__":
    print(f"Script name: {sys.argv[0]}")
    
    if len(sys.argv) > 1:
        print(f"Number of arguments: {len(sys.argv) - 1}")
        print("Arguments passed:")
        for i, arg in enumerate(sys.argv[1:]):
            print(f"  Argument {i+1}: {arg}")
    else:
        print("No arguments provided.")

# How to run from the command line:
# python script_name.py arg1 "another argument" 123
```

For more complex command-line argument parsing (e.g., optional arguments, flags, type checking), the `argparse` module in the standard library is highly recommended.

```python
# Brief example using argparse (save as argparse_example.py)
import argparse

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="A simple script to demonstrate argparse.")
    parser.add_argument("name", help="Your name")
    parser.add_argument("-v", "--verbose", action="store_true", help="Enable verbose output")
    parser.add_argument("--age", type=int, help="Your age")

    args = parser.parse_args()

    print(f"Hello, {args.name}!")
    if args.age:
        print(f"You are {args.age} years old.")
    if args.verbose:
        print("Verbose mode enabled.")

# How to run:
# python argparse_example.py Alice --age 30 -v
# python argparse_example.py Bob
# python argparse_example.py -h (to see help)
```
