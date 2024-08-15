from unittest import TestCase
from Util.CommandParser import CommandParser


class TestCommandParser_Parse(TestCase):
    def test_Parse_error_pattern_01(self):
        # error: コマンドライン引数にnullが指定されました。
        test = CommandParser(0, 0, None)
        self.assertEqual(test.Parse(), None)

    def test_Parse_error_pattern_02(self):
        # error: 「パラメータの最小数」は0以上にしてください。
        test = CommandParser(-1, 0, ['',])
        self.assertEqual(test.Parse(), None)

    def test_Parse_error_pattern_03(self):
        # error: 「パラメータの最大数」は0以上にしてください。
        test = CommandParser(0, -1, ['',])
        self.assertEqual(test.Parse(), None)

    def test_Parse_error_pattern_04(self):
        # error: 「パラメータの最小数」と「パラメータの最大数」の指定に矛盾があります。
        test = CommandParser(1, 0, ['',])
        self.assertEqual(test.Parse(), None)

    def test_Parse_error_pattern_05(self):
        # error: パラメータ数の最小数を満たしません。
        test = CommandParser(1, 1, ['',])
        self.assertEqual(test.Parse(), None)

    def test_Parse_error_pattern_06(self):
        # error: パラメータ数が最大数を超えました。
        test = CommandParser(1, 1, ['param1', 'param2'])
        self.assertEqual(test.Parse(), None)

    def test_Parse_error_pattern_07(self):
        # error: 無効なオプション {arg} が指定されました。
        test = CommandParser(1, 1, ['/aa',])
        self.assertEqual(test.Parse(), None)

    def test_Parse_error_pattern_08(self):
        # error: 無効なオプション {arg} が指定されました。
        test = CommandParser(1, 1, ['--xxxx?',])
        self.assertEqual(test.Parse(), None)

    def test_Parse_error_pattern_09(self):
        # error: 無効なオプション {arg} が指定されました。
        test = CommandParser(1, 1, ['-+',])
        self.assertEqual(test.Parse(), None)

    def test_Parse_pattern_01(self):
        # パラメータ数が0-3の最小数
        test = CommandParser(0, 3, ['',])
        result = test.Parse()
        self.assertEqual(result.GetParameterCount(), 0)

    def test_Parse_pattern_02(self):
        # パラメータ数が0-3の1
        test = CommandParser(0, 3, ['param1',])
        result = test.Parse()
        self.assertEqual(result.GetParameter(0), 'param1')

    def test_Parse_pattern_03(self):
        # パラメータ数が0-3の3
        test = CommandParser(0, 3, ['param1', 'param2', 'param3'])
        result = test.Parse()
        self.assertEqual(result.GetParameter(0), 'param1')
        self.assertEqual(result.GetParameter(1), 'param2')
        self.assertEqual(result.GetParameter(2), 'param3')

    def test_Parse_pattern_04(self):
        # オプション/x
        test = CommandParser(0, 0, ['/x',])
        result = test.Parse()
        self.assertTrue(result.ContainsOption('x'))
        self.assertEqual(result.GetOption('x'), '')

    def test_Parse_pattern_05(self):
        # オプション/x
        test = CommandParser(0, 0, ['/x:yyyy',])
        result = test.Parse()
        self.assertTrue(result.ContainsOption('x'))
        self.assertEqual(result.GetOption('x'), 'yyyy')

    def test_Parse_pattern_06(self):
        # オプション/0
        test = CommandParser(0, 0, ['/0',])
        result = test.Parse()
        self.assertTrue(result.ContainsOption('0'))
        self.assertEqual(result.GetOption('0'), '')

    def test_Parse_pattern_07(self):
        # オプション/9
        test = CommandParser(0, 0, ['/9',])
        result = test.Parse()
        self.assertTrue(result.ContainsOption('9'))
        self.assertEqual(result.GetOption('9'), '')

    def test_Parse_pattern_08(self):
        # オプション/a
        test = CommandParser(0, 0, ['/a',])
        result = test.Parse()
        self.assertTrue(result.ContainsOption('a'))
        self.assertEqual(result.GetOption('a'), '')

    def test_Parse_pattern_09(self):
        # オプション/z
        test = CommandParser(0, 0, ['/z',])
        result = test.Parse()
        self.assertTrue(result.ContainsOption('z'))
        self.assertEqual(result.GetOption('z'), '')

    def test_Parse_pattern_10(self):
        # オプション/a
        test = CommandParser(0, 0, ['/A',])
        result = test.Parse()
        self.assertTrue(result.ContainsOption('A'))
        self.assertEqual(result.GetOption('A'), '')

    def test_Parse_pattern_11(self):
        # オプション/z
        test = CommandParser(0, 0, ['/Z',])
        result = test.Parse()
        self.assertTrue(result.ContainsOption('Z'))
        self.assertEqual(result.GetOption('Z'), '')

    def test_Parse_pattern_12(self):
        # オプション/0:yyyy
        test = CommandParser(0, 0, ['/0:yyyy',])
        result = test.Parse()
        self.assertTrue(result.ContainsOption('0'))
        self.assertEqual(result.GetOption('0'), 'yyyy')

    def test_Parse_pattern_13(self):
        # オプション/9:yyyy
        test = CommandParser(0, 0, ['/9:yyyy',])
        result = test.Parse()
        self.assertTrue(result.ContainsOption('9'))
        self.assertEqual(result.GetOption('9'), 'yyyy')

    def test_Parse_pattern_14(self):
        # オプション/a:yyyy
        test = CommandParser(0, 0, ['/a:yyyy',])
        result = test.Parse()
        self.assertTrue(result.ContainsOption('a'))
        self.assertEqual(result.GetOption('a'), 'yyyy')

    def test_Parse_pattern_15(self):
        # オプション/z:yyyy
        test = CommandParser(0, 0, ['/z:yyyy',])
        result = test.Parse()
        self.assertTrue(result.ContainsOption('z'))
        self.assertEqual(result.GetOption('z'), 'yyyy')

    def test_Parse_pattern_16(self):
        # オプション/a:yyyy
        test = CommandParser(0, 0, ['/A:yyyy',])
        result = test.Parse()
        self.assertTrue(result.ContainsOption('A'))
        self.assertEqual(result.GetOption('A'), 'yyyy')

    def test_Parse_pattern_17(self):
        # オプション/Z:yyyy
        test = CommandParser(0, 0, ['/Z:yyyy',])
        result = test.Parse()
        self.assertTrue(result.ContainsOption('Z'))
        self.assertEqual(result.GetOption('Z'), 'yyyy')

    def test_Parse_pattern_18(self):
        # オプション--09azAZ
        test = CommandParser(0, 0, ['--09azAZ',])
        result = test.Parse()
        self.assertTrue(result.ContainsOption('09azAZ'))
        self.assertEqual(result.GetOption('09azAZ'), '')

    def test_Parse_pattern_19(self):
        # オプション--09azAZ+
        test = CommandParser(0, 0, ['--09azAZ+',])
        result = test.Parse()
        self.assertTrue(result.ContainsOption('09azAZ+'))
        self.assertEqual(result.GetOption('09azAZ+'), '')

    def test_Parse_pattern_20(self):
        # オプション--09azAZ-
        test = CommandParser(0, 0, ['--09azAZ-',])
        result = test.Parse()
        self.assertTrue(result.ContainsOption('09azAZ-'))
        self.assertEqual(result.GetOption('09azAZ-'), '')

    def test_Parse_pattern_21(self):
        # オプション--09azAZ:yyyy
        test = CommandParser(0, 0, ['--09azAZ:yyyy',])
        result = test.Parse()
        self.assertTrue(result.ContainsOption('09azAZ'))
        self.assertEqual(result.GetOption('09azAZ'), 'yyyy')

    def test_Parse_pattern_22(self):
        # オプション--09azAZ+:yyyy
        test = CommandParser(0, 0, ['--09azAZ+:yyyy',])
        result = test.Parse()
        self.assertTrue(result.ContainsOption('09azAZ+'))
        self.assertEqual(result.GetOption('09azAZ+'), 'yyyy')

    def test_Parse_pattern_23(self):
        # オプション--09azAZ-:yyyy
        test = CommandParser(0, 0, ['--09azAZ-:yyyy',])
        result = test.Parse()
        self.assertTrue(result.ContainsOption('09azAZ-'))
        self.assertEqual(result.GetOption('09azAZ-'), 'yyyy')

    def test_Parse_pattern_24(self):
        # オプション-09azAZ
        test = CommandParser(0, 0, ['-09azAZ',])
        result = test.Parse()
        self.assertTrue(result.ContainsOption('0'))
        self.assertTrue(result.ContainsOption('9'))
        self.assertTrue(result.ContainsOption('a'))
        self.assertTrue(result.ContainsOption('z'))
        self.assertTrue(result.ContainsOption('A'))
        self.assertTrue(result.ContainsOption('Z'))
        self.assertEqual(result.GetOption('0'), '')
        self.assertEqual(result.GetOption('9'), '')
        self.assertEqual(result.GetOption('a'), '')
        self.assertEqual(result.GetOption('z'), '')
        self.assertEqual(result.GetOption('A'), '')
        self.assertEqual(result.GetOption('Z'), '')
