from typing import List
from unittest import TestCase
from Util.CommandParameter import CommandParameter


class TestCommandParameter_GetParameter(TestCase):
    def test_GetParameter_error_pattern_01(self):
        p1: List[str] = []
        p2: {str, str} = {}
        p1.append('a')
        p1.append('b')
        p1.append('c')
        test = CommandParameter(p1, p2)
        self.assertEqual(test.GetParameter(-1), '')

    def test_GetParameter_error_pattern_02(self):
        p1: List[str] = []
        p2: {str, str} = {}
        p1.append('a')
        p1.append('b')
        p1.append('c')
        test = CommandParameter(p1, p2)
        self.assertEqual(test.GetParameter(3), '')

    def test_GetParameter_pattern_01(self):
        p1: List[str] = []
        p2: {str, str} = {}
        p1.append('a')
        p1.append('b')
        p1.append('c')
        test = CommandParameter(p1, p2)
        self.assertEqual(test.GetParameter(0), 'a')

    def test_GetParameter_pattern_02(self):
        p1: List[str] = []
        p2: {str, str} = {}
        p1.append('a')
        p1.append('b')
        p1.append('c')
        test = CommandParameter(p1, p2)
        self.assertEqual(test.GetParameter(1), 'b')

    def test_GetParameter_pattern_03(self):
        p1: List[str] = []
        p2: {str, str} = {}
        p1.append('a')
        p1.append('b')
        p1.append('c')
        test = CommandParameter(p1, p2)
        self.assertEqual(test.GetParameter(2), 'c')
