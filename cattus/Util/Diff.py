import filecmp
import difflib


class Diff():
    @staticmethod
    def DiffFile(filename1: str, filename2: str) -> str:
        msg = ''
        cmp: bool = filecmp.cmp(filename1, filename2)
        if not cmp:
            text1: [str] = []
            with open(filename1, mode='r', encoding='utf-8') as f:
                text1 = f.readlines()
            text2: [str] = []
            with open(filename2, mode='r', encoding='utf-8') as f:
                text2 = f.readlines()
            res = difflib.context_diff(text1, text2)
            msg = '\n'.join(res)
            return msg
        else:
            return msg
