from typing import List
from unittest import TestCase
from Util.CommandParameter import CommandParameter


class TestCommandParameter_ContainsOption(TestCase):
    def test_ContainsOption_pattern_01(self):
        p1: List[str] = []
        p2: {str, str} = {}
        p2['a'] = 'b'
        test = CommandParameter(p1, p2)
        self.assertTrue(test.ContainsOption('a'))

    def test_ContainsOption_pattern_02(self):
        p1: List[str] = []
        p2: {str, str} = {}
        p2['a'] = 'b'
        test = CommandParameter(p1, p2)
        self.assertFalse(test.ContainsOption('b'))
