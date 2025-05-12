# Python Data Structures: Lists and Tuples

This README covers essential concepts about Python's list and tuple data structures, their methods, and related operations.

## Table of Contents
1. [Lists](#lists)
2. [Strings vs Lists](#strings-vs-lists)
3. [List Methods](#list-methods)
4. [Lists as Stacks and Queues](#lists-as-stacks-and-queues)
5. [List Comprehensions](#list-comprehensions)
6. [Tuples](#tuples)
7. [Tuples vs Lists](#tuples-vs-lists)
8. [Sequences](#sequences)
9. [Tuple Packing and Unpacking](#tuple-packing-and-unpacking)
10. [The `del` Statement](#the-del-statement)

## Lists

Lists are ordered, mutable collections of items (which can be of different types). They are one of Python's most versatile data structures.

```python
# Creating a list
fruits = ['apple', 'banana', 'cherry']
numbers = [1, 2, 3, 4, 5]
mixed = [1, 'hello', 3.14, True]

# Accessing elements
first_fruit = fruits[0]      # 'apple'
last_fruit = fruits[-1]      # 'cherry'

# Slicing
some_fruits = fruits[1:3]    # ['banana', 'cherry']

# Modifying lists
fruits[1] = 'blueberry'      # Replace an item
fruits.append('orange')      # Add to the end
fruits.insert(1, 'mango')    # Insert at position
fruits.remove('apple')       # Remove first occurrence
```

## Strings vs Lists

### Similarities:
- Both are sequences (ordered collections)
- Support indexing and slicing
- Can be concatenated (`+`) and repeated (`*`)
- Support `len()`, `min()`, `max()`
- Can be iterated over with loops

### Differences:
- **Mutability**: Strings are immutable, lists are mutable
- **Methods**: Different methods available (e.g., strings have `upper()`, lists have `append()`)
- **Content**: Strings store characters, lists can store any data type
- **Memory**: Strings are generally more memory efficient for text

## List Methods

Common list methods include:

```python
numbers = [1, 2, 3, 4, 5]

# Adding elements
numbers.append(6)           # [1, 2, 3, 4, 5, 6]
numbers.extend([7, 8])      # [1, 2, 3, 4, 5, 6, 7, 8]
numbers.insert(0, 0)        # [0, 1, 2, 3, 4, 5, 6, 7, 8]

# Removing elements
numbers.remove(0)           # Removes first occurrence of 0
popped = numbers.pop()      # Removes and returns last item (8)
popped = numbers.pop(0)     # Removes and returns first item (1)

# Other useful methods
numbers.sort()              # Sorts in place
numbers.reverse()           # Reverses in place
count = numbers.count(2)    # Count occurrences of 2
index = numbers.index(3)    # Find index of first 3
numbers.clear()             # Empty the list
```

## Lists as Stacks and Queues

### Stack (LIFO - Last In, First Out)
```python
stack = []
stack.append('a')  # Push
stack.append('b')
stack.append('c')
item = stack.pop()  # Pop - returns 'c'
```

### Queue (FIFO - First In, First Out)
For efficient FIFO operations, use `collections.deque`:
```python
from collections import deque
queue = deque(['a', 'b', 'c'])
queue.append('d')    # Enqueue
item = queue.popleft()  # Dequeue - returns 'a'
```

## List Comprehensions

Concise way to create lists:

```python
# Basic syntax: [expression for item in iterable]
squares = [x**2 for x in range(10)]  # [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

# With condition
odds = [x for x in range(10) if x % 2 == 1]  # [1, 3, 5, 7, 9]

# Nested loops
pairs = [(x, y) for x in [1,2,3] for y in [3,1,4] if x != y]
# [(1, 3), (1, 4), (2, 3), (2, 1), (2, 4), (3, 1), (3, 4)]
```

## Tuples

Tuples are ordered, immutable sequences, typically used to store related pieces of information.

```python
# Creating tuples
point = (10, 20)           # Parentheses are optional
person = 'John', 25, 'NY'  # Tuple packing
empty_tuple = ()
singleton = (5,)            # Note the comma

# Accessing elements
x = point[0]               # 10
name, age, city = person   # Tuple unpacking

# Tuples are immutable
# point[0] = 5  # This would raise a TypeError
```

## Tuples vs Lists

### Use tuples when:
- The data shouldn't change (immutable)
- You need to use it as a dictionary key (tuples are hashable if all elements are hashable)
- Working with database records or function returns
- Performance is critical (tuples are slightly faster)

### Use lists when:
- You need to modify the collection
- You need to add/remove items frequently
- The order or content might change
- You need to use list-specific methods

## Sequences

In Python, a sequence is an ordered collection of items. The main sequence types are:
- Lists: Mutable, dynamic arrays
- Tuples: Immutable sequences
- Strings: Immutable sequences of Unicode characters
- Ranges: Immutable sequences of numbers

Common sequence operations:
```python
seq = [1, 2, 3, 4, 5]

# Membership testing
3 in seq          # True
6 not in seq      # True

# Concatenation
new_seq = seq + [6, 7, 8]

# Repetition
doubled = seq * 2  # [1, 2, 3, 4, 5, 1, 2, 3, 4, 5]

# Length, min, max, sum
length = len(seq)  # 5
minimum = min(seq) # 1
maximum = max(seq) # 5
total = sum(seq)   # 15
```

## Tuple Packing and Unpacking

### Tuple Packing
Creating a tuple by separating values with commas:
```python
person = 'Alice', 30, 'Engineer'  # Packed into a tuple
```

### Sequence Unpacking
Extracting values from a sequence into variables:
```python
name, age, job = person  # Unpacks into name='Alice', age=30, job='Engineer'

# Swap variables
a, b = 10, 20
a, b = b, a  # Swaps values

# Extended unpacking (Python 3+)
first, *rest = [1, 2, 3, 4]  # first=1, rest=[2, 3, 4]
```

## The `del` Statement

The `del` statement removes references to objects and can delete elements from lists or variables from the namespace.

```python
# Deleting variables
x = 10
del x
# print(x)  # Would raise NameError

# Deleting list elements
numbers = [1, 2, 3, 4, 5]
del numbers[1]      # Removes 2: [1, 3, 4, 5]
del numbers[1:3]    # Removes slice: [1, 5]

# Deleting dictionary keys
person = {'name': 'John', 'age': 30}
del person['age']   # Removes the 'age' key

# Deleting entire lists
del numbers         # Removes the reference to the list
```

Remember that `del` removes the reference, not necessarily the object itself (which is handled by Python's garbage collector).