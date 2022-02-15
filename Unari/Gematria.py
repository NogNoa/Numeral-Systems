"""
א-ת
0x05D0-0x05EA
digraphs
0x05F0-0x05F2
"""

סופיות = {'ף', 'ם', 'ץ', 'ך'}
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
        ordnl = ord(self.val) - ord('א')
        ordnl += (self.val in סופיות)

    def __str__(self):
        return self.val

    def __int__(self):
        return {}
