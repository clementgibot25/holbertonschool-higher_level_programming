# Python Inheritance Explained

This document provides a comprehensive explanation of Python's inheritance mechanism, a fundamental concept in object-oriented programming.

## Table of Contents
1. [Superclass, Baseclass, Parentclass](#superclass-baseclass-parentclass)
2. [Subclass](#subclass)
3. [Listing Attributes and Methods](#listing-attributes-and-methods)
4. [Adding New Attributes to Instances](#adding-new-attributes-to-instances)
5. [Basic Inheritance](#basic-inheritance)
6. [Multiple Inheritance](#multiple-inheritance)
7. [The Default Base Class](#the-default-base-class)
8. [Method Overriding](#method-overriding)
9. [Inherited Attributes and Methods](#inherited-attributes-and-methods)
10. [Purpose of Inheritance](#purpose-of-inheritance)
11. [Built-in Functions](#built-in-functions)

## Superclass, Baseclass, Parentclass
A superclass (also known as a base class or parent class) is a class that serves as the foundation for other classes. It defines common attributes and methods that can be inherited by its subclasses. This promotes code reuse and establishes a hierarchical relationship between classes.

```python
class Vehicle:  # Superclass
    def __init__(self, make, model):
        self.make = make
        self.model = model
    
    def start_engine(self):
        return "Engine started"
```

## Subclass
A subclass (or derived class) is a class that inherits from another class. It can:
- Inherit all attributes and methods from its parent class
- Add new attributes and methods
- Override inherited methods
- Extend the functionality of the parent class

```python
class Car(Vehicle):  # Subclass of Vehicle
    def __init__(self, make, model, num_doors):
        super().__init__(make, model)  # Initialize parent class
        self.num_doors = num_doors
    
    def honk(self):  # New method
        return "Beep beep!"
```

## Listing Attributes and Methods
Python provides several ways to inspect a class or instance:

1. `dir()`: Returns a list of all attributes and methods of an object
2. `__dict__`: Returns a dictionary of the object's attributes
3. `help()`: Shows documentation for a class or method

```python
class Example:
    class_attr = "I'm a class attribute"
    
    def __init__(self):
        self.instance_attr = "I'm an instance attribute"
    
    def method(self):
        pass

# Using dir()
print(dir(Example))  # Shows all attributes and methods

# Using __dict__
print(Example.__dict__)  # Shows the class namespace
print(Example().__dict__)  # Shows instance attributes
```

## Adding New Attributes to Instances
In Python, you can add new attributes to an instance at any time, unless the class uses `__slots__` to restrict attribute creation.

```python
class Person:
    def __init__(self, name):
        self.name = name

# Create instance
person = Person("Alice")

# Add new attribute
person.age = 30  # This is allowed
print(person.age)  # 30

# Using __slots__ to restrict attributes
class RestrictedPerson:
    __slots__ = ['name']  # Only 'name' attribute is allowed
    
    def __init__(self, name):
        self.name = name

rp = RestrictedPerson("Bob")
# rp.age = 30  # This would raise an AttributeError
```

## Basic Inheritance
Inheritance is achieved by specifying the parent class in parentheses after the class name.

```python
class Animal:
    def __init__(self, name):
        self.name = name
    
    def speak(self):
        return "Some generic sound"

class Dog(Animal):  # Inherits from Animal
    def speak(self):  # Method overriding
        return "Woof!"

# Usage
dog = Dog("Buddy")
print(dog.name)     # "Buddy" (inherited from Animal)
print(dog.speak())  # "Woof!" (overridden method)
```

## Multiple Inheritance
Python supports multiple inheritance, where a class can inherit from multiple parent classes.

```python
class Flyable:
    def fly(self):
        return "I can fly!"

class Swimmable:
    def swim(self):
        return "I can swim!"

class Duck(Flyable, Swimmable):  # Multiple inheritance
    pass

duck = Duck()
print(duck.fly())   # From Flyable
print(duck.swim())  # From Swimmable
```

## The Default Base Class
In Python 3, all classes implicitly inherit from the `object` class if no other parent is specified.

```python
class MyClass:  # Implicitly inherits from object
    pass

# Is equivalent to
class MyClass(object):
    pass

# Both are instances of object
print(isinstance(MyClass(), object))  # True
```

## Method Overriding
Subclasses can override methods inherited from their parent classes by defining a method with the same name.

```python
class Shape:
    def area(self):
        return "Area not defined"

class Square(Shape):
    def __init__(self, side):
        self.side = side
    
    def area(self):  # Overrides Shape's area method
        return self.side ** 2

# Usage
shape = Shape()
square = Square(4)
print(shape.area())  # "Area not defined"
print(square.area())  # 16
```

## Inherited Attributes and Methods
In Python, all attributes and methods are inherited with some exceptions:
- Private names (those starting with `__`) are name-mangled
- The `__dict__` contains all attributes
- Special methods (like `__init__`) are inherited unless overridden

```python
class Parent:
    def public_method(self):
        return "Public method"
    
    def _protected_method(self):
        return "Protected method (convention only)"
    
    def __private_method(self):
        return "Private method (name mangled)"

class Child(Parent):
    pass

child = Child()
print(child.public_method())     # Works
print(child._protected_method()) # Works (but by convention, should be treated as protected)
# print(child.__private_method())  # Would raise AttributeError
# But this would work (name mangling):
print(child._Parent__private_method())  # Not recommended
```

## Purpose of Inheritance
Inheritance serves several important purposes in object-oriented programming:

1. **Code Reuse**: Avoid duplicating code by inheriting common functionality
2. **Extensibility**: Add new functionality to existing code without modifying it
3. **Maintainability**: Changes in the base class automatically propagate to derived classes
4. **Polymorphism**: Different classes can be treated as instances of the same class
5. **Organization**: Creates a logical hierarchy of classes

## Built-in Functions

### `isinstance(object, classinfo)`
Checks if an object is an instance of a class or a tuple of classes. Also returns True for subclasses.

```python
class Animal: pass
class Dog(Animal): pass

dog = Dog()
print(isinstance(dog, Dog))     # True
print(isinstance(dog, Animal))  # True (because of inheritance)
print(isinstance(dog, (int, str, Animal)))  # True (checks against any in tuple)
```

### `issubclass(class, classinfo)`
Checks if a class is a subclass of another class or a tuple of classes.

```python
class Animal: pass
class Dog(Animal): pass

print(issubclass(Dog, Animal))        # True
print(issubclass(Dog, (int, Animal))) # True (checks against any in tuple)
print(issubclass(Dog, object))        # True (all classes inherit from object)
```

### `type(object)`
Returns the type of an object. Can also be used to create new types dynamically.

```python
# Getting type
print(type(42))          # <class 'int'>
print(type("hello"))     # <class 'str'>

# Creating a class dynamically
DynamicClass = type('DynamicClass', (object,), {'x': 42})
obj = DynamicClass()
print(obj.x)  # 42
```

### `super([type[, object-or-type]])`
Returns a proxy object that delegates method calls to a parent or sibling class.

```python
class Parent:
    def __init__(self, name):
        self.name = name
    
    def greet(self):
        return f"Hello from {self.name}"

class Child(Parent):
    def __init__(self, name, age):
        super().__init__(name)  # Call parent's __init__
        self.age = age
    
    def greet(self):
        parent_greeting = super().greet()
        return f"{parent_greeting}, I'm {self.age} years old"

# Usage
child = Child("Alice", 10)
print(child.greet())  # "Hello from Alice, I'm 10 years old"
```

### When to use each function:
- Use `isinstance()` when you need to check if an object is an instance of a class (including inheritance)
- Use `issubclass()` when you need to check class inheritance relationships
- Use `type()` when you need the exact type of an object or for metaprogramming
- Use `super()` to call parent class methods, especially in method overriding scenarios
