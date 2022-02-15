class אות:

    def __init__(self, char):
        unipt = char.encode("utf-8")
        if b'\xd7\x90' <= unipt <= b'\xd7\xAA':
            self.val = char
        elif b'\xd7\xB0' <= unipt <= b'\xd7\xB2':
            raise ValueError  # Yiddish digraph
        else:
            raise ValueError

    def __str__(self):
        return self.val

    def __int__(self):
        return {}