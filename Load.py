from Hash import *
from Decryptage import *
import os

class Load:
    def __init__(self, file):
        self.file = file

    def load(self):
        text_crypted = open(self.file, "r").read()
        text_decrypted = Decryptage().decrypt(text_crypted)
        return text_decrypted

    def test_if_modified(self):
        text = self.load()
        print(text)
        data, h = text.split('|')
        if Hash(data).hashing() == h:
            print(True)
        else:
            print(False)
            os.remove(self.file)