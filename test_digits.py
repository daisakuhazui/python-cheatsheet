# -*- coding:utf-8 -*-
import unittest
import digits

class TestDigits(unittest.TestCase):
    def test(self):
        self.assertEqual(digits.dig_pow(89, 1), 1)
        self.assertEqual(digits.dig_pow(92, 1), -1)
        self.assertEqual(digits.dig_pow(46288, 3), 51)
