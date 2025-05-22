# Python Object-Oriented Programming (OOP) Guide

## Why Python Programming is Awesome
Python is a powerful, high-level programming language known for its simplicity and readability. Its object-oriented nature allows for clean and efficient code organization, making it ideal for both beginners and experienced developers. Python's extensive standard library and vast ecosystem of packages enable rapid development across various domains.

## Object-Oriented Programming (OOP)
OOP is a programming paradigm based on the concept of "objects" that can contain data (attributes) and code (methods). It helps in structuring programs by bundling related properties and behaviors into individual objects.

## First-Class Everything
In Python, everything is an object, including functions, classes, and primitive types. This means you can:
- Assign them to variables
- Pass them as arguments to functions
- Return them from functions
- Store them in data structures

## Class
A class is a blueprint for creating objects. It defines the attributes and methods that the created objects will have.

```python
class MyClass:
    pass
```

## Object and Instance
- An **object** is an instance of a class.
- An **instance** is a specific object created from a particular class.

```python
my_object = MyClass()  # my_object is an instance of MyClass
```

### Difference Between Class and Object/Instance
- A **class** is a blueprint/template.
- An **object/instance** is a concrete "thing" based on that blueprint.

## Attribute
An attribute is a variable that belongs to an object or class.

```python
class Person:
    def __init__(self, name):
        self.name = name  # name is an instance attribute
```

## Access Modifiers
- **Public**: Accessible from anywhere (default in Python)
- **Protected**: Indicated by a single underscore `_` (convention only)
- **Private**: Indicated by double underscore `__` (name mangling occurs)

```python
class Example:
    def __init__(self):
        self.public = "public"     # public
        self._protected = "protected"  # protected (by convention)
        self.__private = "private"    # private (name mangled to _Example__private)
```

## Self
`self` is a reference to the current instance of the class. It's used to access variables and methods associated with the current object.

## Method
A method is a function that's associated with an object.

```python
class Dog:
    def bark(self):  # method
        return "Woof!"
```

## `__init__` Method
The `__init__` method is a special method that gets called when an object is instantiated. It's used to initialize the object's attributes.

```python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
```

## OOP Principles
- **Data Abstraction**: Hiding complex implementation details and showing only the necessary features.
- **Encapsulation**: Restricting direct access to some of an object's components.
- **Information Hiding**: Making attributes private to prevent direct access.

## Property
A property allows you to use getter and setter methods while accessing an attribute like a regular attribute.

```python
class Circle:
    def __init__(self, radius):
        self._radius = radius
    
    @property
    def radius(self):
        return self._radius
    
    @radius.setter
    def radius(self, value):
        if value < 0:
            raise ValueError("Radius cannot be negative")
        self._radius = value
```

### Difference Between Attribute and Property
- An **attribute** is a simple variable stored in an object.
- A **property** is a special kind of attribute that uses getter/setter methods.

## Pythonic Getters and Setters
Python encourages using the `@property` decorator instead of traditional getter/setter methods.

## `__str__` and `__repr__` Methods
- `__str__`: Returns a human-readable string representation of the object.
- `__repr__`: Returns an unambiguous string representation of the object, typically used for debugging.

```python
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __str__(self):
        return f"Point({self.x}, {self.y})"
    
    def __repr__(self):
        return f"Point(x={self.x}, y={self.y})"
```

### Difference Between `__str__` and `__repr__`
- `__str__` is for end-users (readable)
- `__repr__` is for developers (unambiguous)

## Class Attribute
A class attribute is shared by all instances of the class.

```python
class Dog:
    species = "Canis familiaris"  # class attribute
    
    def __init__(self, name):
        self.name = name  # instance attribute
```

### Difference Between Instance and Class Attributes
- **Instance attributes**: Specific to each instance
- **Class attributes**: Shared among all instances

## Class Method
A method that's bound to the class and not the instance. It takes `cls` as the first parameter.

```python
class MyClass:
    count = 0
    
    @classmethod
    def increment_count(cls):
        cls.count += 1
        return cls.count
```

## Static Method
A method that doesn't receive any implicit first argument. It's just a function that belongs to the class's namespace.

```python
class MathUtils:
    @staticmethod
    def add(x, y):
        return x + y
```

## Dynamic Attributes
You can add attributes to instances dynamically:

```python
class Person:
    pass

p = Person()
p.name = "John"  # Adding attribute dynamically
```

## Binding Attributes
Attributes can be bound to both instances and classes:

```python
class MyClass:
    pass

# Class attribute
MyClass.class_attr = 10

# Instance attribute
obj = MyClass()
obj.instance_attr = 20
```

## `__dict__`
- `__dict__` is a dictionary containing the module's, class's, or instance's namespace.
- For instances, it contains instance attributes.
- For classes, it contains class attributes and methods.

## Attribute Lookup
Python follows this order when looking up attributes:
1. Instance attributes
2. Class attributes
3. Parent class attributes
4. `__getattr__` method (if defined)

## `getattr()` Function
Gets the value of a named attribute of an object.

```python
class Person:
    def __init__(self, name):
        self.name = name

p = Person("Alice")
print(getattr(p, 'name'))  # Output: Alice
print(getattr(p, 'age', 30))  # Returns 30 if 'age' doesn't exist
```
