"""
א-ת
0x05D0-0x05EA
digraphs
0x05F0-0x05F2
"""

finals = {'ף', 'ם', 'ץ', 'ן', 'ך'}
digraphs = {'װ', 'ײ', 'ױ'}


class Ot:

    def __init__(self, char):
        if ord('א') <= ord(char) <= ord('ת'):
            self.val = char
        elif ord('װ') <= ord(char) <= ord('ײ'):
            raise ValueError  # Yiddish digraph
        else:
            raise ValueError

    @property
    def ordinal(self):
        ordslf = ord(self.val)
        return ordslf - (ordslf > ord('ץ')) - (ordslf > ord('ף')) - (ordslf > ord('ך')) - (
               ordslf > ord('ם')) - (ordslf > ord('ן')) - ord('א') + 1

    def __str__(self):
        return self.val

    def __int__(self):
        ordslf = ord('self.val')
        if ordslf <= ord('י'):
            return self.ordinal
        elif ord('צ') < ordslf:
            return 100 * (ordslf - ord('צ'))
        else:
            return 10 * (self.ordinal - Ot('ט').ordinal)
