class MorseMidiTranslator():
    def __init__(self):
        self.table = {
            'a': '.-',
            'b': '-...',
            'c': '-.-.',
            'd': '-..',
            'e': '.',
            'f': '',
            'g': '--.',
            'h': '....',
            'i': '..',
            'j': '.---',
            'k': '-.-',
            'l': '',
            'm': '--',
            'n': '',
            'o': '---',
            'p': '',
            'q': '...-',
            'r': '.-.',
            's': '...',
            't': '',
            'u': '',
            'v': '',
            'w': '',
            'x': '-..-',
            'y': '',
            'z': '',
        };

    def Translate(string text):
        for ch in text:
