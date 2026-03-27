from Hash import *
from Cryptage import *

class Save:
    def __init__(self, data , file):
        self.data = data
        self.file = file

    def crypted_data(self):
        text_hash = Hash(self.data).returning()
        text_crypt = Cryptage(text_hash).encrypt()
        return str(text_crypt)
    
    def save(self):
        with open(self.file, "w") as f:
            f.write(self.crypted_data())