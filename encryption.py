# Here will be the encryption logic:
"""
- Caesar Cipher
- Pleifer Cipher
- Base64
- etc
"""

class Cipher():
    def __init__(self, message):
        self.text_to_encrypt = message
        self.encrypted_text = ""
        

class CaesarCipher(Cipher):
    def __init__(self, key, message):
        super().__init__(message)
        try:
            self.shift = int(key)
        except:
            self.shift = 0


    def encrypt(self):
        for sign in self.text_to_encrypt:
            sign_num = ord(sign)
            if sign_num <= 90 and sign_num >= 41:
                sign_num = (sign_num + self.shift) % 90
                if sign_num < 41:
                    sign_num += 41
            elif sign_num <= 122 and sign_num >= 97:
                sign_num = (sign_num + self.shift) % 122
                if sign_num < 97:
                    sign_num += 97
            self.encrypted_text += chr(sign_num)
        
        return str(self.encrypted_text)
    
    # def decrypt(self):
    #     for sign in self.text_to_encrypt:
    #         sign_num = ord(sign)
    #         if sign_num <= 90 and sign_num >= 41:
    #             sign_num = (sign_num - self.shift)
    #             if sign_num < 41:
    #                 sign_num += 41
    #         elif sign_num <= 122 and sign_num >= 97:
    #             sign_num = (sign_num + self.shift) % 122
    #             if sign_num < 97:
    #                 sign_num += 97
    #         self.encrypted_text += chr(sign_num)
        
    #     return str(self.encrypted_text)

