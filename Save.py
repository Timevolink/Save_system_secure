from Hash import *
from Cryptage import *
from Decryptage import *

class Save:
    def __init__(self, data):
        self.data = data

    def crypted_data(self):
        text_hash = Hash(self.data).returning()
        text_crypt = Cryptage(text_hash).encrypt()
        return str(text_crypt)
    
    def save(self):
        with open("save.dat", "w") as f:
            f.write(self.crypted_data())

    def load(self):
        text_crypted = open("save.dat", "r").read()
        text_decrypted = Decryptage().decrypt(text_crypted)
        return text_decrypted
