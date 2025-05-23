#!/usr/bin/python3
"""
9-rectangle.py: Defines a Rectangle class with instance tracking,
custom print symbol, comparison, square creation, width, height, area,
perimeter, string representation, and deletion message.
"""


class Rectangle:
    """
    Defines a rectangle with instance tracking, custom print symbol,
    comparison, square creation, width, height, area, perimeter,
    string representation, and deletion message.

    Class Attributes:
        number_of_instances (int): Tracks the number of Rectangle instances.
        print_symbol (any): Symbol used for string representation.

    Instance Attributes:
        __width (int): The width of the rectangle
        __height (int): The height of the rectangle
    """

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """
        Initialize a new Rectangle instance and increment the instance counter.

        Args:
            width (int, optional): The width of the rectangle. Defaults to 0.
            height (int, optional): The height of the rectangle. Defaults to 0.
        """
        self.width = width
        self.height = height
        type(self).number_of_instances += 1

    @property
    def width(self):
        """int: Gets or sets the width of the rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        """
        Set the width of the rectangle.

        Args:
            value (int): The width value to set.

        Raises:
            TypeError: If width is not an integer.
            ValueError: If width is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """int: Gets or sets the height of the rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        """
        Set the height of the rectangle.

        Args:
            value (int): The height value to set.

        Raises:
            TypeError: If height is not an integer.
            ValueError: If height is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """
        Calculate the area of the rectangle.

        Returns:
            int: The area of the rectangle (width * height).
        """
        return self.__width * self.__height

    def perimeter(self):
        """
        Calculate the perimeter of the rectangle.

        Returns:
            int: The perimeter of the rectangle (2 * (width + height)).
                  Returns 0 if either width or height is 0.
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        """
        Return a string representation of the rectangle using print_symbol.

        Returns:
            str: The string representation of the rectangle.
                 Returns an empty string if width or height is 0.
        """
        if self.__width == 0 or self.__height == 0:
            return ""
        symbol = str(self.print_symbol)
        rectangle_rows = []
        for _ in range(self.__height):
            rectangle_rows.append(symbol * self.__width)
        return '\n'.join(rectangle_rows)

    def __repr__(self):
        """
        Return a string representation of the rectangle for recreation.

        Returns:
            str: A string that can be used with eval() to
            create a new instance.
        """
        return f"Rectangle({self.__width}, {self.__height})"

    def __del__(self):
        """
        Print a message when an instance of Rectangle is deleted
        and decrement the instance counter.
        """
        type(self).number_of_instances -= 1
        print("Bye rectangle...")

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """
        Return the bigger rectangle based on the area.

        Args:
            rect_1 (Rectangle): The first rectangle to compare.
            rect_2 (Rectangle): The second rectangle to compare.

        Returns:
            Rectangle: The rectangle with the larger area.
                     Returns rect_1 if both have the same area.

        Raises:
            TypeError: If rect_1 or rect_2 is not an instance of Rectangle.
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")

        if rect_1.area() >= rect_2.area():
            return rect_1
        return rect_2

    @classmethod
    def square(cls, size=0):
        """
        Create a new Rectangle instance with equal width and height.

        Args:
            size (int, optional): The size of the square's sides.
            Defaults to 0.


        Returns:
            Rectangle: A new Rectangle instance with width == height == size.
        """
        return cls(size, size)
