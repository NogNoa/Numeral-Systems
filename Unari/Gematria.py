"""
א-ת
0x05D0-0x05EA
digraphs
0x05F0-0x05F2
"""

סופיות = {'ף', 'ם', 'ץ', 'ן', 'ך'}
digraphs = {'װ', 'ײ', 'ױ'}


class אות:

    def __init__(self, char):
        if ord('א') <= ord(char) <= ord('ת'):
            self.val = char
        elif ord('װ') <= ord(char) <= ord('ײ'):
            raise ValueError  # Yiddish digraph
        else:
            raise ValueError

    @property
    def ordinal(self):
        return ord(self.val) - (ord(self.val) > ord('ץ')) - (ord(self.val) > ord('ף')) - (ord(self.val) > ord('ך')) - (
               ord(self.val) > ord('ם')) - (ord(self.val) > ord('ן')) - ord('א')

    def __str__(self):
        return self.val

    def __int__(self):
        return {}
