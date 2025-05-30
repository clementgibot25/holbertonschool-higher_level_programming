# Python Advanced OOP Concepts

This guide covers essential Object-Oriented Programming (OOP) concepts in Python, focusing on advanced class design and inheritance patterns.

## Table of Contents
1. [Abstract Classes](#abstract-classes)
2. [Interfaces and Duck Typing](#interfaces-and-duck-typing)
3. [Subclassing Standard Base Classes](#subclassing-standard-base-classes)
4. [Method Overriding](#method-overriding)
5. [Multiple Inheritance](#multiple-inheritance)
6. [Mixins](#mixins)

## Abstract Classes

Abstract classes are classes that cannot be instantiated and are meant to be subclassed. They define a common interface for their subclasses.

### Key Points:
- Use the `abc` module to create abstract base classes
- Decorate methods with `@abstractmethod` to make them abstract
- Subclasses must implement all abstract methods
- Abstract classes can have concrete methods with implementations

```python
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass
    
    @abstractmethod
    def perimeter(self):
        pass

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def area(self):
        return self.width * self.height
    
    def perimeter(self):
        return 2 * (self.width + self.height)
```

## Interfaces and Duck Typing

Python uses "duck typing" - if it walks like a duck and quacks like a duck, it's a duck. There's no explicit interface keyword, but we can use abstract base classes to define interfaces.

### Key Points:
- Focus on object behavior rather than type
- Objects are used based on their methods and attributes, not their class
- Use `hasattr()` and `isinstance()` for type checking when needed

```python
class Quackable:
    def quack(self):
        pass

class Duck(Quackable):
    def quack(self):
        return "Quack!"

class Person:
    def quack(self):
        return "I'm quacking like a duck!"

def make_it_quack(duck_like):
    if hasattr(duck_like, 'quack'):
        return duck_like.quack()
    return "Can't quack!"
```

## Subclassing Standard Base Classes

Python allows you to subclass built-in types like `list`, `dict`, and `set` to create custom data structures.

### Key Points:
- Inherit from built-in types
- Override or extend existing methods
- Call parent class methods using `super()`

```python
class CustomList(list):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.history = []
    
    def append(self, item):
        self.history.append(f"Added: {item}")
        return super().append(item)
    
    def pop(self, index=-1):
        item = super().pop(index)
        self.history.append(f"Removed: {item}")
        return item
```

## Method Overriding

Subclasses can provide a specific implementation of a method that is already defined in their parent class.

### Key Points:
- Same method name as in parent class
- Can call parent's method using `super()`
- Used to extend or modify parent class behavior

```python
class Animal:
    def speak(self):
        return "Some generic sound"

class Dog(Animal):
    def speak(self):
        return "Woof!"

class Cat(Animal):
    def speak(self):
        return "Meow!"

class LazyCat(Cat):
    def speak(self):
        parent_sound = super().speak()
        return f"{parent_sound}... zzz"
```

## Multiple Inheritance

Python supports multiple inheritance, allowing a class to inherit from multiple parent classes.

### Key Points:
- List multiple parent classes in the class definition
- Method Resolution Order (MRO) determines the search order
- Use `super()` to call parent class methods
- Be cautious of the "diamond problem"

```python
class A:
    def method(self):
        return "A"

class B(A):
    def method(self):
        return "B"

class C(A):
    def method(self):
        return "C"

class D(B, C):
    pass

# Method Resolution Order (MRO)
print(D.mro())  # Shows the method resolution order
```

## Mixins

Mixins are a way to provide optional features to classes through multiple inheritance.

### Key Points:
- Small, focused classes that provide specific functionality
- Not meant to be instantiated directly
- Name should end with "Mixin" by convention
- Used to share behavior between unrelated classes

```python
class JSONMixin:
    def to_json(self):
        import json
        return json.dumps(self.__dict__)

class XMLMixin:
    def to_xml(self):
        # Simplified XML conversion
        attrs = ' '.join(f'{k}="{v}"' for k, v in self.__dict__.items())
        return f"<{self.__class__.__name__} {attrs} />"

class Person(JSONMixin, XMLMixin):
    def __init__(self, name, age):
        self.name = name
        self.age = age

# Usage
p = Person("Alice", 30)
print(p.to_json())  # Uses JSONMixin
print(p.to_xml())    # Uses XMLMixin
```

## Best Practices

1. **Favor composition over inheritance** when possible
2. Use **mixins** for cross-cutting concerns
3. Keep inheritance hierarchies **shallow and simple**
4. Document the **intended behavior** of abstract methods
5. Use **type hints** to make interfaces more explicit
6. Consider **composition** before reaching for multiple inheritance

## Further Reading
- [Python's ABC documentation](https://docs.python.org/3/library/abc.html)
- [Python's Data Model](https://docs.python.org/3/reference/datamodel.html)
- [PEP 3119 - Introducing Abstract Base Classes](https://www.python.org/dev/peps/pep-3119/)
- [PEP 3135 - New Super](https://www.python.org/dev/peps/pep-3135/)

Remember that while these features are powerful, they should be used judiciously to keep your code maintainable and understandable.
