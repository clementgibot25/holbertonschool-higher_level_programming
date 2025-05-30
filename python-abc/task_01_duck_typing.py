#!/usr/bin/python3
"""
Duck typing example with shapes.

This module demonstrates duck typing by defining different shape classes
that implement the same interface (area and perimeter methods).
"""


import math
from abc import ABC, abstractmethod


class Shape(ABC):
    """Abstract base class for shapes with area and perimeter methods."""

    @abstractmethod
    def area(self):
        """Calculate the area of the shape."""
        pass

    @abstractmethod
    def perimeter(self):
        """Calculate the perimeter of the shape."""
        pass


class Rectangle(Shape):
    """Rectangle shape implementation."""

    def __init__(self, width, height):
        """Initialize rectangle with width and height."""
        self.width = width
        self.height = height

    def area(self):
        """Calculate the area of the rectangle."""
        return self.width * self.height

    def perimeter(self):
        """Calculate the perimeter of the rectangle."""
        return 2 * (self.width + self.height)


class Circle(Shape):
    """Circle shape implementation."""

    def __init__(self, radius):
        """Initialize circle with radius."""
        self.radius = radius

    def area(self):
        """Calculate the area of the circle."""
        return math.pi * (self.radius ** 2)

    def perimeter(self):
        """Calculate the circumference of the circle."""
        return 2 * math.pi * self.radius


def shape_info(shape):
    """Print information about a shape.

    Args:
        shape: An object that implements area() and perimeter() methods.
    """
    print(f"Area: {shape.area()}")
    print(f"Perimeter: {shape.perimeter()}")


if __name__ == "__main__":
    rect = Rectangle(4, 7)
    circle = Circle(5)

    shape_info(rect)
    shape_info(circle)
