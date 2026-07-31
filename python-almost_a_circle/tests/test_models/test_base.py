#!/usr/bin/python3
"""Defines unit tests for models/base.py."""
import os
import json
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestBase_instantiation(unittest.TestCase):
    """Unit tests for testing instantiation of the Base class."""

    def test_id_public(self):
        b = Base(12)
        self.assertEqual(b.id, 12)

    def test_id_none_auto_assigned(self):
        Base._Base__nb_objects = 0
        b1 = Base()
        b2 = Base()
        self.assertEqual(b1.id, 1)
        self.assertEqual(b2.id, 2)

    def test_id_zero(self):
        b = Base(0)
        self.assertEqual(b.id, 0)

    def test_id_negative(self):
        b = Base(-5)
        self.assertEqual(b.id, -5)

    def test_no_args(self):
        with self.assertRaises(TypeError):
            Base(1, 2)


class TestBase_to_json_string(unittest.TestCase):
    """Unit tests for testing to_json_string method of Base class."""

    def test_none(self):
        self.assertEqual(Base.to_json_string(None), "[]")

    def test_empty_list(self):
        self.assertEqual(Base.to_json_string([]), "[]")

    def test_list_of_dictionaries(self):
        list_dicts = [{"id": 1, "width": 10, "height": 4}]
        json_string = Base.to_json_string(list_dicts)
        self.assertEqual(json.loads(json_string), list_dicts)

    def test_return_type_is_str(self):
        self.assertIsInstance(Base.to_json_string([{"id": 1}]), str)

    def test_too_many_args(self):
        with self.assertRaises(TypeError):
            Base.to_json_string([{"id": 1}], [{"id": 2}])


class TestBase_from_json_string(unittest.TestCase):
    """Unit tests for testing from_json_string method of Base class."""

    def test_none(self):
        self.assertEqual(Base.from_json_string(None), [])

    def test_empty_string(self):
        self.assertEqual(Base.from_json_string(""), [])

    def test_valid_json_string(self):
        list_dicts = [{"id": 1, "width": 10, "height": 4}]
        json_string = json.dumps(list_dicts)
        self.assertEqual(Base.from_json_string(json_string), list_dicts)

    def test_return_type_is_list(self):
        json_string = json.dumps([{"id": 1}])
        self.assertIsInstance(Base.from_json_string(json_string), list)

    def test_too_many_args(self):
        with self.assertRaises(TypeError):
            Base.from_json_string("[]", "[]")


class TestBase_save_to_file(unittest.TestCase):
    """Unit tests for testing save_to_file method of Base class."""

    def tearDown(self):
        for fname in ("Rectangle.json", "Square.json"):
            if os.path.exists(fname):
                os.remove(fname)

    def test_save_to_file_rectangle(self):
        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4)
        Rectangle.save_to_file([r1, r2])
        self.assertTrue(os.path.exists("Rectangle.json"))
        with open("Rectangle.json", "r") as f:
            content = json.load(f)
        self.assertEqual(len(content), 2)

    def test_save_to_file_none(self):
        Rectangle.save_to_file(None)
        with open("Rectangle.json", "r") as f:
            self.assertEqual(f.read(), "[]")

    def test_save_to_file_empty_list(self):
        Rectangle.save_to_file([])
        with open("Rectangle.json", "r") as f:
            self.assertEqual(f.read(), "[]")

    def test_save_to_file_overwrites(self):
        Rectangle.save_to_file([Rectangle(1, 1)])
        Rectangle.save_to_file([Rectangle(2, 2), Rectangle(3, 3)])
        with open("Rectangle.json", "r") as f:
            content = json.load(f)
        self.assertEqual(len(content), 2)

    def test_save_to_file_square(self):
        s1 = Square(5)
        Square.save_to_file([s1])
        self.assertTrue(os.path.exists("Square.json"))


class TestBase_create(unittest.TestCase):
    """Unit tests for testing the create method of Base class."""

    def test_create_rectangle(self):
        r1 = Rectangle(3, 5, 1)
        r1_dict = r1.to_dictionary()
        r2 = Rectangle.create(**r1_dict)
        self.assertEqual(str(r1), str(r2))
        self.assertIsNot(r1, r2)

    def test_create_square(self):
        s1 = Square(5, 2, 3, 15)
        s1_dict = s1.to_dictionary()
        s2 = Square.create(**s1_dict)
        self.assertEqual(str(s1), str(s2))
        self.assertIsNot(s1, s2)


class TestBase_load_from_file(unittest.TestCase):
    """Unit tests for testing load_from_file method of Base class."""

    def tearDown(self):
        for fname in ("Rectangle.json", "Square.json"):
            if os.path.exists(fname):
                os.remove(fname)

    def test_load_from_file_no_file(self):
        if os.path.exists("Rectangle.json"):
            os.remove("Rectangle.json")
        self.assertEqual(Rectangle.load_from_file(), [])

    def test_load_from_file_rectangle(self):
        r1 = Rectangle(10, 7, 2, 8, 5)
        r2 = Rectangle(2, 4, 0, 0, 6)
        Rectangle.save_to_file([r1, r2])
        loaded = Rectangle.load_from_file()
        self.assertEqual(len(loaded), 2)
        self.assertEqual(str(loaded[0]), str(r1))
        self.assertEqual(str(loaded[1]), str(r2))

    def test_load_from_file_square(self):
        s1 = Square(5, 1, 2, 10)
        Square.save_to_file([s1])
        loaded = Square.load_from_file()
        self.assertEqual(len(loaded), 1)
        self.assertEqual(str(loaded[0]), str(s1))

    def test_load_from_file_return_type(self):
        Rectangle.save_to_file([Rectangle(1, 1)])
        loaded = Rectangle.load_from_file()
        self.assertIsInstance(loaded[0], Rectangle)


if __name__ == "__main__":
    unittest.main()
