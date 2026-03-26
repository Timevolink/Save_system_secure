class Cryptage:
    def __init__(self, data):
        self.data = data
        self.key = "Super_personne"

    def encrypt(self):
        result = ""
        for i in range(len(self.data)):
            k = self.key[i % len(self.key)]
            result += chr(ord(self.data[i]) ^ ord(k))
        return str(result)