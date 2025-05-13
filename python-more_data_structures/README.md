# Data Structures in Python

## What are Sets and How to Use Them
A **set** is an unordered collection of unique, immutable elements. Sets are mutable, meaning you can add or remove items, but the items themselves must be immutable (e.g., numbers, strings, tuples).

**Creating a set:**
```python
my_set = {1, 2, 3}
my_set2 = set([1, 2, 3, 2])  # Duplicates are removed automatically
```

Sets are useful for removing duplicates, testing membership, and performing mathematical set operations.

## Most Common Methods of Set and How to Use Them
- `add(elem)`: Add an element to the set.
- `remove(elem)`: Remove an element; raises KeyError if not present.
- `discard(elem)`: Remove an element if present; does nothing if not.
- `pop()`: Remove and return an arbitrary element.
- `clear()`: Remove all elements.
- `union(other_set)`: Return a new set with elements from both sets.
- `intersection(other_set)`: Return a new set with elements common to both.
- `difference(other_set)`: Elements in the set but not in the other.

**Example:**
```python
A = {1, 2, 3}
B = {3, 4, 5}
A.add(6)            # {1, 2, 3, 6}
A.union(B)          # {1, 2, 3, 4, 5, 6}
A.intersection(B)   # {3}
A.difference(B)     # {1, 2, 6}
```

## When to Use Sets Versus Lists
- Use **sets** when:
  - You need to store unique elements only (no duplicates).
  - You need fast membership testing (`in` keyword).
- Use **lists** when:
  - You need to preserve order or allow duplicates.
  - You need indexing or slicing.

## How to Iterate Into a Set
Sets are iterable:
```python
for item in my_set:
    print(item)
```
Note: The order of elements is not guaranteed.

## What are Dictionaries and How to Use Them
A **dictionary** is an unordered collection of key-value pairs. Keys must be unique and immutable. Values can be of any type.

**Creating a dictionary:**
```python
my_dict = {'name': 'Alice', 'age': 30}
my_dict2 = dict(name='Bob', age=25)
```
Access values by key:
```python
print(my_dict['name'])  # Alice
```

## When to Use Dictionaries Versus Lists or Sets
- Use **dictionaries** when:
  - You need to associate values with unique keys.
  - Fast lookup by key is important.
- Use **lists** when:
  - You have a simple sequence of items.
  - Order and duplicates matter.
- Use **sets** when:
  - You only care about unique items and do not need key-value pairs.

## What is a Key in a Dictionary
A **key** is the unique identifier for a value in a dictionary. Keys must be immutable types (e.g., strings, numbers, tuples).

## How to Iterate Over a Dictionary
You can iterate over keys, values, or both:
```python
# Iterate over keys
for key in my_dict:
    print(key)
# Iterate over values
for value in my_dict.values():
    print(value)
# Iterate over key-value pairs
for key, value in my_dict.items():
    print(key, value)
```

## What is a Lambda Function
A **lambda function** is a small anonymous function defined with the `lambda` keyword. It can have any number of arguments but only one expression.

**Example:**
```python
add = lambda x, y: x + y
print(add(2, 3))  # 5
```

## What are the Map, Reduce, and Filter Functions
- `map(function, iterable)`: Applies a function to every item in an iterable.
- `filter(function, iterable)`: Filters items for which the function returns `True`.
- `reduce(function, iterable)`: Applies a rolling computation to sequential pairs (must import from `functools`).

**Examples:**
```python
nums = [1, 2, 3, 4]
# map
squared = list(map(lambda x: x**2, nums))  # [1, 4, 9, 16]
# filter
evens = list(filter(lambda x: x % 2 == 0, nums))  # [2, 4]
# reduce
from functools import reduce
sum_all = reduce(lambda x, y: x + y, nums)  # 10
```
