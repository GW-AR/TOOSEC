import random

# Here will be the encryption logic:
"""
- Caesar Cipher
- Playfair Cipher
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
            if sign_num <= 90 and sign_num >= 65:
                sign_num = (sign_num + self.shift) % 91
                if sign_num < 65:
                    sign_num += 65
            elif sign_num <= 122 and sign_num >= 97:
                sign_num = (sign_num + self.shift) % 123
                if sign_num < 97:
                    sign_num += 97
            self.encrypted_text += chr(sign_num)
        
        return str(self.encrypted_text)
    
    def decrypt(self):
        for sign in self.text_to_encrypt:
            sign_num = ord(sign)
            if sign_num <= 90 and sign_num >= 65:
                sign_num = (sign_num - self.shift)
                if sign_num < 65:
                    sign_num = (sign_num + 26)
            elif sign_num <= 122 and sign_num >= 97:
                sign_num = (sign_num - self.shift)
                if sign_num < 97:
                    sign_num = (sign_num + 26)
            self.encrypted_text += chr(sign_num)
        
        return str(self.encrypted_text)


class PlayfairCipher(Cipher):
    def __init__(self, key, message):
        super().__init__(message)
        try:
            self.keyword = key
        except:
            self.keyword = ""
        self.matrix = self.create_matrix()
        self.diagrams = self.create_diagrams()

    def create_matrix(self):
        matrix = [chr(i) for i in range(65, 91) if i not in (73, 74)]
        matrix.insert(8, "IJ")
        # remove duplicated letters
        key_word = ""
        for letter in self.keyword:
            if letter not in key_word:
                key_word += letter
        # create matrix
        key_word = key_word[::-1]
        for letter in key_word.upper():
            if letter in "IJ":
                matrix.remove("IJ")
                matrix.insert(0, "IJ")
            else:
                matrix.remove(letter)
                matrix.insert(0, letter)
        new_matrix = [matrix[i:i+5] for i in range(0,20,5)]
        return new_matrix
    
    def create_diagrams(self):
        diagrams = []
        message = [letter for letter in self.text_to_encrypt.upper() if letter.isalpha()]
        for i in range(0, len(message), 2):
            try:
                if message[i] == message[i+1]:
                    message.insert(i+1, "X")
            except:
                message.append("X")
        if len(message) % 2 != 0:
            message.append("X")
        self.text_to_encrypt = "".join(message)

        diagrams = [[char for char in self.text_to_encrypt[i:i+2]] for i in range(0, len(self.text_to_encrypt), 2)]
        return diagrams


    def encrypt(self):
        encrypted_diagrams = []
        for diagram in self.diagrams:
            letter_indexes = []
            bi = ""
            for letter in diagram:
                for i, row in enumerate(self.matrix):
                    for j, val in enumerate(row):
                        if letter == val:
                            letter_indexes.append((i, j))
            # same row
            if letter_indexes[0][0] == letter_indexes[1][0]:
                bi += self.matrix[letter_indexes[0][0]][(letter_indexes[0][1]+1)%5]
                bi += self.matrix[letter_indexes[1][0]][(letter_indexes[1][1]+1)%5]
            # same column
            elif letter_indexes[0][1] == letter_indexes[1][1]:
                bi += self.matrix[(letter_indexes[0][0]+1)%5][letter_indexes[0][1]]
                bi += self.matrix[(letter_indexes[1][0]+1)%5][letter_indexes[0][1]]
            # different column and row
            else:
                bi += self.matrix[letter_indexes[0][0]][letter_indexes[1][1]]
                bi += self.matrix[letter_indexes[1][0]][letter_indexes[0][1]]
            
            encrypted_diagrams.append(bi)
            
        self.encrypted_text = " ".join(encrypted_diagrams)
        return str(self.encrypted_text)





# cipher = PlayfairCipher("monarchy","testing")
# print(cipher.matrix)
# print(cipher.diagrams)
# print(cipher.encrypt())