# Here will be the encryption logic:
"""
- Caesar Cipher
- Pleifer Cipher
- Base64
- etc
"""

from bs4 import BeautifulSoup


class Cipher():
    def __init__(self):
        self.text_to_encrypt = ""
        self.encrypted_text = "hej"
        

class CaesarCipher(Cipher):
    def __init__(self):
        super().__init__()
        self.shift = 0


cezar = CaesarCipher()
print(cezar.encrypted_text)


