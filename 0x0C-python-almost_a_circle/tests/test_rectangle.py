#!/usr/bin/python3
"""
contains test for RECTANGLE class
"""

import unittest
import sys
from io import StringIO
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    """Rectangle test class"""

    def test_rectangle(self):
        """test rectangle created"""
        r1 = Rectangle(10, 2, id=90)
        r2 = Rectangle(2, 10, id=34)
        r3 = Rectangle(10, 2, 2, 5, 12)

        with self.subTest("check id value"):
            self.assertEqual(r1.id, 90)
            self.assertEqual(r2.id, 34)
            self.assertEqual(r3.id, 12)
        with self.subTest("check default values"):
            self.assertEqual(r1.width, 10)
            self.assertEqual(r1.height, 2)
            self.assertEqual(r2.x, 0)
            self.assertEqual(r2.y, 0)
            self.assertEqual(r3.x, 2)
            self.assertEqual(r3.y, 5)

    def test_rectangle_args(self):
        """test values in args"""
        self.assertRaises(TypeError, Rectangle, "w", 2)
        self.assertRaises(TypeError, Rectangle, 2, "h")
        self.assertRaises(TypeError, Rectangle, 2, 4, "x", 2, 12)
        self.assertRaises(TypeError, Rectangle, 2, 4, 2, "y", 12)
        self.assertRaises(ValueError, Rectangle, 0, 2)
        self.assertRaises(ValueError, Rectangle, 2, 0)
        self.assertRaises(ValueError, Rectangle, 2, 4, -1, 1, 12)
        self.assertRaises(ValueError, Rectangle, 2, 4, 1, -1, 12)

    def test_rectangle_methods(self):
        """test rectangle methods"""
        r1 = Rectangle(4, 6, id=14)
        r2 = Rectangle(3, 2, 2, 2)

        with self.subTest("area of rectangle"):
            self.assertEqual(r1.area(), 24)

        with self.subTest("str repr of rectangle"):
            self.assertEqual(r1.__str__(), "[Rectangle] (14) 0/0 - 4/6")

        with self.subTest("dislay rectangle using #"):
            captured_string = StringIO()
            sys.stdout = captured_string
            r1.display()
            output_value = captured_string.getvalue().strip()
            sys.stdout = sys.__stdout__
            exp_value = "####\n####\n####\n####\n####\n####"
            self.assertEqual(output_value, exp_value)

        with self.subTest("display rectangle along with axis"):
            captured_str = StringIO()
            sys.stdout = captured_str
            r2.display()
            output_str = captured_str.getvalue()
            sys.stdout = sys.__stdout__
            exp_str = "\n\n  ###\n  ###\n"
            self.assertEqual(exp_str, output_str)

        with self.subTest("update method with args and kwargs"):
            r1.update(width=1, x=2)
            self.assertEqual(r1.__str__(), "[Rectangle] (14) 2/0 - 1/6")
            r1.update(height=1)
            self.assertEqual(r1.__str__(), "[Rectangle] (14) 2/0 - 1/1")
            r1.update(y=1, width=2, x=3, id=89)
            self.assertEqual(r1.__str__(), "[Rectangle] (89) 3/1 - 2/1")

        with self.subTest("to dictionary method"):
            r5 = Rectangle(10, 2, 1, 9, 60)
            exp_value = {'x': 1, 'y': 9, 'id': 60, 'height': 2, 'width': 10}
            self.assertEqual(r5.to_dictionary(), exp_value)
