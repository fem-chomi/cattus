from typing import List
from unittest import TestCase
from Util.CommandParameter import CommandParameter


class TestCommandParameter_GetOption(TestCase):
    def test_GetOption_error_pattern_01(self):
        p1: List[str] = []
        p2: {str, str} = {}
        p2['a'] = 'b'
        test = CommandParameter(p1, p2)
        self.assertEqual(test.GetOption('b'), '')

    def test_GetOption_pattern_01(self):
        p1: List[str] = []
        p2: {str, str} = {}
        p2['a'] = 'b'
        test = CommandParameter(p1, p2)
        self.assertEqual(test.GetOption('a'), 'b')
