from typing import List
from unittest import TestCase
from Util.CommandParameter import CommandParameter


class TestCommandParameter_GetParameterCount(TestCase):
    def test_GetParameterCount_pattern_01(self):
        p1: List[str] = []
        p2: {str, str} = {}
        p1.append('a')
        p1.append('b')
        p1.append('c')
        test = CommandParameter(p1, p2)
        self.assertEqual(test.GetParameterCount(), 3)
