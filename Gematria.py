"""
א-ת
0x05D0-0x05EA
digraphs
0x05F0-0x05F2
"""

finals = {'ף', 'ם', 'ץ', 'ן', 'ך'}
digraphs = {'װ', 'ײ', 'ױ'}


def ordinal(char):
    ord_call = ord(char)
    return ord_call - (ord_call > ord('ץ')) - (ord_call > ord('ף')) - (ord_call > ord('ך')) - (
           ord_call > ord('ם')) - (ord_call > ord('ן')) - ord('א') + 1


class YiddishError(ValueError):
    pass


class Ot:

    def __init__(self, char):
        if ord('א') <= ord(char) <= ord('ת'):
            self.val = char
        elif char in digraphs:
            raise YiddishError  # Yiddish digraph
        else:
            raise ValueError

    @property
    def ordinal(self):
        return ordinal(self.val)

    def __str__(self):
        return self.val

    def __int__(self):
        ordslf = self.ordinal
        if ordslf <= ordinal('י'):
            return ordslf
        elif ordinal('צ') < ordslf:
            return 100 * (ordslf - ordinal('צ'))
        else:
            return 10 * (ordslf - ordinal('ט'))

    def extra_int(self):
        if self.val in finals:
            return {'ץ': 900, 'ף': 800, 'ן': 700, 'ם': 600, 'ך': 500}[self.val]
        else:
            return int(self)


class Otiot:
    def __init__(self, chari: str):
        try:
            self.val = (Ot(char) for char in chari)
        except YiddishError:
            # exception isn't caught
            chari.replace("װ", "וו").replace("ײ", "יי").replace("ױ", "וי")
            self.val = (Ot(char) for char in chari)

    def __str__(self):
        return "".join(str(char) for char in self.val)

    def __int__(self):
        return sum(int(char) for char in self.val)



