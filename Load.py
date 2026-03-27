from Hash import *
from Decryptage import *
import os

class Load:
    def __init__(self, file = "save1.dat" , key = "Super_personne"):
        self.file = file
        self.key = key

    def load(self):
        text_crypted = open(self.file, "r").read()
        text_decrypted = Decryptage(self.key).decrypt(text_crypted)
        return text_decrypted

    def test_if_modified(self):
        text = self.load()
        print(text)
        full_data = text.split('|')
        if len(full_data) != 2:
            print(False)
            os.remove(self.file)
        else:
            data, h = text.split('|')
            if Hash(data).hashing() == h:
                print(True)
            else:
                print(False)
                os.remove(self.file)