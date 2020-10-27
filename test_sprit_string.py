# -*- coding:utf-8 -*-
import unittest
import sprit_string


class TestSpritString(unittest.TestCase):
  def test(self):
    tests = (
        ("asdfadsf", ['as', 'df', 'ad', 'sf']),
        ("asdfads", ['as', 'df', 'ad', 's_']),
        ("", []),
        ("x", ["x_"]),
    )

    for inp, exp in tests:
        self.assertEqual(sprit_string.solution(inp), exp)
