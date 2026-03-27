class Decryptage:
    def __init__(self, key):
        self.key = key

    def decrypt(self, data):
        result = ""
        for i in range(len(data)):
            k = self.key[i % len(self.key)]
            result += chr(ord(data[i]) ^ ord(k))
        return str(result)