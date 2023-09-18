#!/usr/bin/python3
"""
Tests for base class module
"""
import unittest
import json
from models.base import Base


class BaseClassTest(unittest.TestCase):
    """
    Base class test
    """

    def test_no_arg_base(self):
        """
        test id value
        """
        b1 = Base()
        b2 = Base()
        self.assertEqual(b1.id, b2.id - 1)

    def test_id_args(self):
        """
        id set to value
        """
        b1 = Base(5)
        self.assertEqual(b1.id, 5)

    def test_id_None(self):
        """
        set id automatically
        """
        b1 = Base(None)
        self.assertEqual(b1.id, 1)

    def test_increment(self):
        """
        id increased
        """
        b1 = Base()
        b2 = Base()
        b3 = Base()
        self.assertEqual(b2.id, b1.id + 1)


class Test_methods(unittest.TestCase):
    """
    test run on to_json_string method
    """
    def test_to_json_string(self):
        """
        doc tesy
        """
        b = Base()
        self.assertEqual(b.to_json_string([]), ("[]"))
        self.assertEqual(b.to_json_string(None), ("[]"))
        self.assertEqual((b.to_json_string([{'id': 14}])), json.dumps([{"id": 14}]))

    def test_from_json_string(self):
        """
        test doc
        """
        b = Base()
        self.assertEqual(b.from_json_string(None), [])
        a = ""
        self.assertEqual(b.from_json_string(a), [])
        c = json.loads('[{"id": 14}]')
        self.assertEqual(b.from_json_string('[{"id": 14}]'), c)


if __name__ == "__main__":
    unittest.main()
