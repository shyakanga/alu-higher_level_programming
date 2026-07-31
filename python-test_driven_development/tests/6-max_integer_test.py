#!/usr/bin/python3
"""Unittest for max_integer([..])"""
import unittest

max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """TestCase class for max_integer function"""

    def test_ordered_list(self):
        """Test with an ordered list of integers"""
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_unordered_list(self):
        """Test with an unordered list of integers"""
        self.assertEqual(max_integer([1, 3, 4, 2]), 4)

    def test_max_at_beginning(self):
        """Test list with max value at the start"""
        self.assertEqual(max_integer([4, 3, 2, 1]), 4)

    def test_empty_list(self):
        """Test an empty list"""
        self.assertEqual(max_integer([]), None)

    def test_one_element_list(self):
        """Test list with a single element"""
        self.assertEqual(max_integer([7]), 7)

    def test_floats(self):
        """Test list with float numbers"""
        self.assertEqual(max_integer([1.53, 6.33, -9.12, 15.6, 6.0]), 15.6)

    def test_ints_and_floats(self):
        """Test list with integers and floats"""
        self.assertEqual(max_integer([1.53, 15, 6.33, -9, 15.6, 6]), 15.6)

    def test_string(self):
        """Test with a string"""
        self.assertEqual(max_integer("Python"), 'y')

    def test_list_of_strings(self):
        """Test list of strings"""
        self.assertEqual(max_integer(["apple", "zebra", "banana"]), "zebra")

    def test_negative_integers(self):
        """Test list of negative integers"""
        self.assertEqual(max_integer([-1, -2, -3, -4]), -1)


if __name__ == '__main__':
    unittest.main()
