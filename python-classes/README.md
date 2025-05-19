# Python Classes & OOP Concepts

## What is OOP?
Object-Oriented Programming (OOP) is a programming paradigm based on organizing code into objects, which combine data and behavior. OOP aims to make code more modular, reusable, and easier to maintain by modeling real-world entities as objects.

## “First-class everything”
In Python, everything is treated as an object, including functions, classes, and even modules. This is known as "first-class everything," meaning you can pass, assign, and manipulate these entities just like any other variable.

## What is a class?
A class is a blueprint for creating objects. It defines the structure (attributes) and behaviors (methods) that the objects created from the class will have.

## What is an object and an instance?
An object is a concrete occurrence of a class. When a class is instantiated, the resulting entity is called an instance or object of that class. In Python, the terms object and instance are often used interchangeably.

## What is the difference between a class and an object or instance?
A class is the definition or template, while an object (or instance) is a specific instantiation of that template with its own unique data.

## What is an attribute?
An attribute is a variable that belongs to a class or an instance. Attributes store data about the object or class.

## What are and how to use public, protected and private attributes?
- **Public attributes**: Can be accessed from anywhere. (e.g., `self.name`)
- **Protected attributes**: Indicated by a single underscore (e.g., `_name`). By convention, should not be accessed outside the class or its subclasses.
- **Private attributes**: Indicated by double underscores (e.g., `__name`). These are name-mangled to prevent accidental access from outside the class.

## What is self?
`self` is a reference to the current instance of the class. It is used to access attributes and methods within the class.

## What is a method?
A method is a function defined inside a class that operates on instances of that class (using `self`).

## What is the special __init__ method and how to use it?
`__init__` is the constructor method in Python. It is called automatically when a new instance of the class is created, and is used to initialize the object's attributes.

Example:
```python
class Person:
    def __init__(self, name):
        self.name = name
```

## What is Data Abstraction, Data Encapsulation, and Information Hiding?
- **Data Abstraction**: Hiding complex implementation details and showing only the necessary features.
- **Data Encapsulation**: Bundling data (attributes) and methods that operate on the data within a class.
- **Information Hiding**: Restricting access to certain details of an object, often using private/protected attributes.

## What is a property?
A property in Python allows you to define methods that can be accessed like attributes, often used for controlled access to private attributes.

Example:
```python
class Person:
    def __init__(self, name):
        self._name = name

    @property
    def name(self):
        return self._name
```

## What is the difference between an attribute and a property in Python?
- **Attribute**: A variable stored in an object or class.
- **Property**: A special kind of attribute managed by getter, setter, and deleter methods, allowing logic to be run on access or assignment.

## What is the Pythonic way to write getters and setters in Python?
Use the `@property` decorator for getters and `@<property>.setter` for setters, instead of explicit getter/setter methods.

Example:
```python
class Person:
    def __init__(self, name):
        self._name = name

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value
```

## How to dynamically create arbitrary new attributes for existing instances of a class?
You can assign new attributes to an instance at runtime:
```python
person = Person("Alice")
person.age = 30  # Adds a new attribute 'age' to the instance
```

## How to bind attributes to object and classes?
- **Instance attribute**: `instance.attr = value`
- **Class attribute**: `ClassName.attr = value`

## What is the __dict__ of a class and/or instance of a class and what does it contain?
`__dict__` is a dictionary containing all the writable attributes of an object (instance or class). It maps attribute names to their values.

Example:
```python
print(person.__dict__)
```

## How does Python find the attributes of an object or class?
Python looks for attributes in the following order:
1. Instance's `__dict__`
2. Class's `__dict__`
3. Parent classes (following the Method Resolution Order, MRO)

## How to use the getattr function?
`getattr(obj, 'attr', default)` is used to access an attribute by name. If the attribute does not exist, it returns the default value (if provided) or raises an `AttributeError`.

Example:
```python
name = getattr(person, 'name', 'Unknown')
```

## What is the Method Resolution Order (MRO)?
The Method Resolution Order (MRO) is the order in which Python looks for methods and attributes in a class hierarchy. It follows a specific order:
1. Current class
2. Parent classes in the order they are defined
3. Built-in object class

Example:
```python
class A:
    def method(self):
        print("A")

class B(A):
    def method(self):
        print("B")

class C(A):
    def method(self):
        print("C")

class D(B, C):
    pass

print(D.mro())
```
Output:
```python
[<class '__main__.D'>, <class '__main__.B'>, <class '__main__.C'>, <class '__main__.A'>, <class 'object'>]
```
