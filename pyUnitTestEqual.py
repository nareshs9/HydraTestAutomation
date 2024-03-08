#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
_______________________________________________________________________

_______________________________________________________________________

\file    pyUnitTestEqual.py

_______________________________________________________________________

"""
import unittest


class PyUnitTestEqual(unittest.TestCase):

    def test_RNTN_True(self):
        value1 = 5
        value2 = 5
        self.assertEqual(value1, value2)

    def test_RNTN_False(self):
        value1 = 4
        value2 = 5
        self.assertEqual(value1, value2)

if __name__ == '__main__':
    unittest.main()
