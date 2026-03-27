from Hash import *
from Cryptage import *

class Save:
    def __init__(self, data = None, file = "save1.dat", key = "Super_personne"):
        self.data = data
        self.file = file
        self.key = key

    def crypted_data(self):
        text_hash = Hash(self.data).returning()
        text_crypt = Cryptage(text_hash, self.key).encrypt()
        return str(text_crypt)
    
    def save(self):
        with open(self.file, "w") as f:
            f.write(self.crypted_data())