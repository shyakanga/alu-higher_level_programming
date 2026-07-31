#!/usr/bin/python3
"""Defines unit tests for models/square.py."""
import os
import io
import sys
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestSquare_instantiation(unittest.TestCase):
    """Unit tests for testing instantiation of the Square class."""

    def test_is_rectangle_subclass(self):
        self.assertIsInstance(Square(5), Rectangle)

    def test_is_base_subclass(self):
        self.assertIsInstance(Square(5), Base)

    def test_one_arg(self):
        s = Square(5)
        self.assertEqual((s.width, s.height, s.x, s.y), (5, 5, 0, 0))

    def test_two_args(self):
        s = Square(2, 2)
        self.assertEqual((s.width, s.height, s.x), (2, 2, 2))

    def test_three_args(self):
        s = Square(3, 1, 3)
        self.assertEqual((s.width, s.height, s.x, s.y), (3, 3, 1, 3))

    def test_four_args_with_id(self):
        s = Square(3, 1, 3, 99)
        self.assertEqual(s.id, 99)

    def test_no_args(self):
        with self.assertRaises(TypeError):
            Square()


class TestSquare_validation(unittest.TestCase):
    """Unit tests for testing attribute validation of Square."""

    def test_size_not_int(self):
        with self.assertRaises(TypeError):
            Square("5")

    def test_size_negative(self):
        with self.assertRaises(ValueError):
            Square(-1)

    def test_size_zero(self):
        with self.assertRaises(ValueError):
            Square(0)

    def test_x_negative(self):
        with self.assertRaises(ValueError):
            Square(5, -1)

    def test_y_negative(self):
        with self.assertRaises(ValueError):
            Square(5, 0, -1)

    def test_x_str(self):
        with self.assertRaises(TypeError):
            Square(1, "2")

    def test_y_str(self):
        with self.assertRaises(TypeError):
            Square(1, 2, "3")

class TestSquare_save_to_file(unittest.TestCase):
    """Unit tests for testing save_to_file method of Square class."""

    def tearDown(self):
        if os.path.exists("Square.json"):
            os.remove("Square.json")

    def test_save_to_file_none(self):
        Square.save_to_file(None)
        with open("Square.json", "r") as f:
            self.assertEqual(f.read(), "[]")

    def test_save_to_file_empty_list(self):
        Square.save_to_file([])
        with open("Square.json", "r") as f:
            self.assertEqual(f.read(), "[]")


class TestSquare_size(unittest.TestCase):
    """Unit tests for testing the size getter/setter of Square."""

    def test_size_getter(self):
        s = Square(5)
        self.assertEqual(s.size, 5)

    def test_size_setter_updates_width_height(self):
        s = Square(5)
        s.size = 10
        self.assertEqual(s.width, 10)
        self.assertEqual(s.height, 10)

    def test_size_setter_invalid_type(self):
        s = Square(5)
        with self.assertRaises(TypeError) as e:
            s.size = "9"
        self.assertEqual(str(e.exception), "width must be an integer")

    def test_size_setter_invalid_value(self):
        s = Square(5)
        with self.assertRaises(ValueError) as e:
            s.size = -1
        self.assertEqual(str(e.exception), "width must be > 0")


class TestSquare_area(unittest.TestCase):
    """Unit tests for testing the area method of Square."""

    def test_area(self):
        self.assertEqual(Square(5).area(), 25)
        self.assertEqual(Square(2, 2).area(), 4)


class TestSquare_display(unittest.TestCase):
    """Unit tests for testing the display method of Square."""

    def test_display(self):
        s = Square(2)
        captured = io.StringIO()
        sys.stdout = captured
        s.display()
        sys.stdout = sys.__stdout__
        self.assertEqual(captured.getvalue(), "##\n##\n")

    def test_display_with_offset(self):
        s = Square(3, 1, 3)
        captured = io.StringIO()
        sys.stdout = captured
        s.display()
        sys.stdout = sys.__stdout__
        expected = "\n\n\n ###\n ###\n ###\n"
        self.assertEqual(captured.getvalue(), expected)


class TestSquare_str(unittest.TestCase):
    """Unit tests for testing the __str__ method of Square."""

    def test_str(self):
        s = Square(5, 0, 0, 1)
        self.assertEqual(str(s), "[Square] (1) 0/0 - 5")

    def test_str_with_offset(self):
        s = Square(3, 1, 3, 2)
        self.assertEqual(str(s), "[Square] (2) 1/3 - 3")


class TestSquare_update(unittest.TestCase):
    """Unit tests for testing the update method of Square."""

    def test_update_args_all(self):
        s = Square(5, 0, 0, 1)
        s.update(89, 2, 3, 4)
        self.assertEqual(str(s), "[Square] (89) 3/4 - 2")

    def test_update_args_partial(self):
        s = Square(5, 0, 0, 1)
        s.update(1, 2)
        self.assertEqual(str(s), "[Square] (1) 0/0 - 2")

    def test_update_kwargs(self):
        s = Square(5, 0, 0, 1)
        s.update(size=7, id=89, y=1)
        self.assertEqual(str(s), "[Square] (89) 0/1 - 7")

    def test_update_kwargs_skipped_if_args(self):
        s = Square(5, 0, 0, 1)
        s.update(50, size=99)
        self.assertEqual(s.id, 50)
        self.assertEqual(s.size, 5)


class TestSquare_to_dictionary(unittest.TestCase):
    """Unit tests for testing to_dictionary method of Square."""

    def test_to_dictionary_keys_values(self):
        s = Square(10, 2, 1, 1)
        expected = {"id": 1, "size": 10, "x": 2, "y": 1}
        self.assertEqual(s.to_dictionary(), expected)

    def test_to_dictionary_type(self):
        self.assertIsInstance(Square(1).to_dictionary(), dict)

    def test_to_dictionary_roundtrip(self):
        s1 = Square(10, 2, 1)
        s2 = Square(1, 1)
        s2.update(**s1.to_dictionary())
        self.assertEqual(str(s1), str(s2))


if __name__ == "__main__":
    unittest.main()
