class אות:

    def __init__(self, char):
        unipt = char.encode("utf-8")
        if b'\xd7\x90' <= unipt <= b'\xd7\xAA' or \
            b'\xd7\xB0' <= unipt <= b'\xd7\xB2':
            self.val = char

    def yid_seperate(self,char):
