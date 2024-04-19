#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    def test_max(self):
        self.assertEqual(max_integer([1, 5, 7, 3]), 7)
        self.assertEqual(max_integer([3.5, 6.2, 1.9]), 6.2)
        self.assertEqual(max_integer([5.4, 8.1, 7, 8]), 8.1)
        self.assertEqual(max_integer([-2, 2.2, -4]), 2.2)
        self.assertEqual(max_integer([9.2, -9.1, 9]), 9.2)
        self.assertEqual(max_integer([-3, -7, -4]), -3)
        self.assertEqual(max_integer([-6, 0, 5, 1]), 5)
        self.assertEqual(max_integer([1]), 1)
        self.assertEqual(max_integer([-9.7, 9.7, 9, 9, 0]), 9.7)
        self.assertEqual(max_integer([]), None)

    def test_types(self):
        self.assertRaises(TypeError, max_integer, ["lol", 4, 2])

if __name__ == "__main__":
    unittest.main()

