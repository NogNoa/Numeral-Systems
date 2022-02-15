class אות:

    def __init__(self, char):
        unipt = char.encode("utf-8")
        if b'\xd7\x90' <= unipt <= b'\xd7\xAA':
            self.val = char
        elif b'\xd7\xB0' <= unipt <= b'\xd7\xB2':
            return

class Yid(אות):
    def __init__(self,char):
        super().__init__(char)


