from typing import List
from unittest import TestCase
from Util.CommandParameter import CommandParameter


class TestCommandParameter_init(TestCase):
    def test_init_pattern_01(self):
        p1: List[str] = []
        p2: {str, str} = {}
        p1.append('a')
        p2['b'] = 'c'
        test = CommandParameter(p1, p2)
        self.assertEqual(test.GetParameterCount(), 1)

    def test_init_pattern_02(self):
        p1: List[str] = []
        p2: {str, str} = {}
        p1.append('a')
        p2['b'] = 'c'
        test = CommandParameter(p1, p2)
        self.assertTrue(test.ContainsOption('b'))
