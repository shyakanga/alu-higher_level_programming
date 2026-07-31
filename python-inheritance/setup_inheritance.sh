#!/usr/bin/bash

# Create tests directory
mkdir -p tests

# Create mandatory README.md
cat << 'README_EOF' > README.md
# Python - Inheritance

This project covers OOP inheritance, class hierarchies, method overriding, super(), and built-in functions like `isinstance`, `issubclass`, `type`, and `dir`.
README_EOF

# Task 0: 0-lookup.py
cat << 'FILE_0' > 0-lookup.py
#!/usr/bin/python3
"""Module that defines a lookup function."""


def lookup(obj):
    """Returns the list of available attributes and methods of an object."""
    return dir(obj)
FILE_0

# Task 1: 1-my_list.py
cat << 'FILE_1' > 1-my_list.py
#!/usr/bin/python3
"""Module that defines a MyList class."""


class MyList(list):
    """Class that inherits from list with a sorted print method."""

    def print_sorted(self):
        """Prints the list in ascending sorted order."""
        print(sorted(self))
FILE_1

# Task 1 Test: tests/1-my_list.txt
cat << 'FILE_1_TEST' > tests/1-my_list.txt
The ``1-my_list`` module
========================

Using ``MyList``
----------------

Testing MyList class:

    >>> MyList = __import__('1-my_list').MyList
    >>> my_list = MyList()
    >>> my_list
    []
    >>> my_list.print_sorted()
    []
    >>> my_list.append(1)
    >>> my_list.append(4)
    >>> my_list.append(2)
    >>> my_list.append(3)
    >>> my_list.append(5)
    >>> print(my_list)
    [1, 4, 2, 3, 5]
    >>> my_list.print_sorted()
    [1, 2, 3, 4, 5]
    >>> print(my_list)
    [1, 4, 2, 3, 5]

Testing with negative numbers:

    >>> my_list2 = MyList()
    >>> my_list2.append(-1)
    >>> my_list2.append(-5)
    >>> my_list2.append(0)
    >>> my_list2.print_sorted()
    [-5, -1, 0]
FILE_1_TEST

# Task 2: 2-is_same_class.py
cat << 'FILE_2' > 2-is_same_class.py
#!/usr/bin/python3
"""Module that checks exact object class instance."""


def is_same_class(obj, a_class):
    """Returns True if obj is exactly an instance of a_class."""
    return type(obj) is a_class
FILE_2

# Task 3: 3-is_kind_of_class.py
cat << 'FILE_3' > 3-is_kind_of_class.py
#!/usr/bin/python3
"""Module that checks object instance or inherited class instance."""


def is_kind_of_class(obj, a_class):
    """Returns True if obj is instance of, or inherited from, a_class."""
    return isinstance(obj, a_class)
FILE_3

# Task 4: 4-inherits_from.py
cat << 'FILE_4' > 4-inherits_from.py
#!/usr/bin/python3
"""Module that checks if an object inherits from a class."""


def inherits_from(obj, a_class):
    """Returns True if obj is an instance of subclass of a_class."""
    return issubclass(type(obj), a_class) and type(obj) is not a_class
FILE_4

# Task 5: 5-base_geometry.py
cat << 'FILE_5' > 5-base_geometry.py
#!/usr/bin/python3
"""Module that defines an empty BaseGeometry class."""


class BaseGeometry:
    """An empty class representing base geometry."""

    pass
FILE_5

# Task 6: 6-base_geometry.py
cat << 'FILE_6' > 6-base_geometry.py
#!/usr/bin/python3
"""Module that defines a BaseGeometry class."""


class BaseGeometry:
    """A class representing base geometry."""

    def area(self):
        """Raises an Exception indicating area is not implemented."""
        raise Exception("area() is not implemented")
FILE_6

# Task 7: 7-base_geometry.py
cat << 'FILE_7' > 7-base_geometry.py
#!/usr/bin/python3
"""Module that defines a BaseGeometry class with integer validation."""


class BaseGeometry:
    """A class representing base geometry with area and validation."""

    def area(self):
        """Raises an Exception indicating area is not implemented."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validates if value is a positive integer."""
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
FILE_7

# Task 7 Test: tests/7-base_geometry.txt
cat << 'FILE_7_TEST' > tests/7-base_geometry.txt
The ``7-base_geometry`` module
==============================

Using ``BaseGeometry``
----------------------

Testing BaseGeometry:

    >>> BaseGeometry = __import__('7-base_geometry').BaseGeometry
    >>> bg = BaseGeometry()

Testing area():

    >>> try:
    ...     bg.area()
    ... except Exception as e:
    ...     print("[{}] {}".format(e.__class__.__name__, e))
    [Exception] area() is not implemented

Testing valid integers:

    >>> bg.integer_validator("my_int", 12)
    >>> bg.integer_validator("width", 89)

Testing non-integer inputs:

    >>> try:
    ...     bg.integer_validator("name", "John")
    ... except Exception as e:
    ...     print("[{}] {}".format(e.__class__.__name__, e))
    [TypeError] name must be an integer

    >>> try:
    ...     bg.integer_validator("bool_val", True)
    ... except Exception as e:
    ...     print("[{}] {}".format(e.__class__.__name__, e))
    [TypeError] bool_val must be an integer

    >>> try:
    ...     bg.integer_validator("float_val", 3.14)
    ... except Exception as e:
    ...     print("[{}] {}".format(e.__class__.__name__, e))
    [TypeError] float_val must be an integer

    >>> try:
    ...     bg.integer_validator("list_val", [1, 2])
    ... except Exception as e:
    ...     print("[{}] {}".format(e.__class__.__name__, e))
    [TypeError] list_val must be an integer

Testing non-positive integers:

    >>> try:
    ...     bg.integer_validator("age", 0)
    ... except Exception as e:
    ...     print("[{}] {}".format(e.__class__.__name__, e))
    [ValueError] age must be greater than 0

    >>> try:
    ...     bg.integer_validator("distance", -4)
    ... except Exception as e:
    ...     print("[{}] {}".format(e.__class__.__name__, e))
    [ValueError] distance must be greater than 0
FILE_7_TEST

# Task 8: 8-rectangle.py
cat << 'FILE_8' > 8-rectangle.py
#!/usr/bin/python3
"""Module that defines a Rectangle class inheriting from BaseGeometry."""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """A class representing a rectangle."""

    def __init__(self, width, height):
        """Initializes width and height after validation."""
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
FILE_8

# Task 9: 9-rectangle.py
cat << 'FILE_9' > 9-rectangle.py
#!/usr/bin/python3
"""Module that defines a Rectangle class with area and str representation."""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """A class representing a rectangle."""

    def __init__(self, width, height):
        """Initializes width and height after validation."""
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        """Calculates and returns the area of the rectangle."""
        return self.__width * self.__height

    def __str__(self):
        """Returns string representation of the rectangle."""
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
FILE_9

# Task 10: 10-square.py
cat << 'FILE_10' > 10-square.py
#!/usr/bin/python3
"""Module that defines a Square class inheriting from Rectangle."""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """A class representing a square."""

    def __init__(self, size):
        """Initializes size after validation."""
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
FILE_10

# Task 11: 11-square.py
cat << 'FILE_11' > 11-square.py
#!/usr/bin/python3
"""Module that defines a Square class with custom str representation."""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """A class representing a square."""

    def __init__(self, size):
        """Initializes size after validation."""
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def __str__(self):
        """Returns string representation of the square."""
        return "[Square] {}/{}".format(self.__size, self.__size)
FILE_11

# Grant execution permissions to Python scripts
chmod +x *.py

echo "All inheritance project files and tests successfully created and configured!"
