#!/usr/bin/python3
"""
contains test for Square class
"""

import unittest
import sys
from io import StringIO
from models.square import Square


class TestSquare(unittest.TestCase):
    """Square test class"""

    def test_square(self):
        """test square created"""
        s1 = Square(5, id=58)
        s2 = Square(3, 2, 3, 67)
        with self.subTest("check id value"):
            self.assertEqual(s1.id, 58)
            self.assertEqual(s2.id, 67)
        with self.subTest("check default values"):
            self.assertEqual(s1.size, 5)
            self.assertEqual(s2.size, 3)
            self.assertEqual(s2.x, 2)
            self.assertEqual(s2.y, 3)

    def test_square_args(self):
        """test values in args"""
        self.assertRaises(TypeError, Square, "w")
        self.assertRaises(TypeError, Square, 2, "h")
        self.assertRaises(TypeError, Square, 2, 4, "x", 12)
        self.assertRaises(ValueError, Square, 0)
        self.assertRaises(ValueError, Square, 2, -1, 0, 12)
        self.assertRaises(ValueError, Square, 2, 3, -1, 12)

    def test_square_methods(self):
        """test square methods"""
        s1 = Square(4, id=14)
        s2 = Square(3, 2, 2)

        with self.subTest("area of square"):
            self.assertEqual(s1.area(), 16)

        with self.subTest("str repr of square"):
            self.assertEqual(s1.__str__(), "[Square] (14) 0/0 - 4")

        with self.subTest("dislay square using #"):
            captured_string = StringIO()
            sys.stdout = captured_string
            s1.display()
            output_value = captured_string.getvalue().strip()
            sys.stdout = sys.__stdout__
            exp_value = "####\n####\n####\n####"
            self.assertEqual(output_value, exp_value)

        with self.subTest("display square along with axis"):
            captured_str = StringIO()
            sys.stdout = captured_str
            s2.display()
            output_str = captured_str.getvalue()
            sys.stdout = sys.__stdout__
            exp_str = "\n\n  ###\n  ###\n  ###\n"
            self.assertEqual(exp_str, output_str)

        with self.subTest("update method with args and kwargs"):
            s1.update(size=7, x=2)
            self.assertEqual(s1.__str__(), "[Square] (14) 2/0 - 7")
            s1.update(y=1)
            self.assertEqual(s1.__str__(), "[Square] (14) 2/1 - 7")
            s1.update(y=1, size=2, x=3, id=89)
            self.assertEqual(s1.__str__(), "[Square] (89) 3/1 - 2")

        with self.subTest("to dictionary method"):
            s5 = Square(10, 2, 1, 66)
            exp_value = {'id': 66, 'x': 2, 'size': 10, 'y': 1}
            self.assertEqual(s5.to_dictionary(), exp_value)
