class change:
    @staticmethod
    def encrypt(string):
        encrypt = ""
        for i in range(len(string)):
            integer1 = int(string[i]) * 2 + 65
            integer2 = int(string[i]) * 2 + 70
            encrypt = encrypt + chr(integer1) + chr(integer2)
        return encrypt

    @staticmethod
    def decrypt(string):
        decrypt = ""
        for i in range(len(string)):
            if i % 2 == 0:
                decrypt = decrypt + str((ord(string[i]) - 65) / 2)
        return decrypt