import random


special_chars_list = [
    '!', '@', '#', '$', '%', '^', '&', '*', '(', ')',
    '-', '_', '=', '+', '[', ']', '{', '}', '|', '\\',
    ':', ';', '"', "'", '<', '>', ',', '.', '?', '/',
    '`', '~']

lowercase_letters = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g',
    'h', 'i', 'j', 'k', 'l', 'm', 'n',
    'o', 'p', 'q', 'r', 's', 't', 'u',
    'v', 'w', 'x', 'y', 'z'
]

class Password():
    def __init__(self, length, contain_uppercase, contain_char, min_char, contain_numbers, min_numbers):
        self.length = int(length)
        if contain_uppercase == "on":
            self.contain_uppercase = True
        else:
            self.contain_uppercase = False
        if contain_char == "on":
            self.contain_char = True
        else:
            self.contain_char = False
        self.min_special_char = int(min_char)
        if contain_numbers == "on":
            self.contain_numbers = True
        else:
            self.contain_numbers = False
        self.min_numbers = int(min_numbers)

        self.number_of_characters = 0
        self.number_of_numbers = 0


    def generate_password(self):
        password_list = []

        #chars
        if self.contain_char:
            self.number_of_characters = random.randint(self.min_special_char, (self.length // 2))
            for number in range( 0 , self.number_of_characters + 1):
                char = random.choice(special_chars_list)
                password_list.append(char)

        #numbers
        if self.contain_numbers:
            self.number_of_numbers = random.randint(self.min_numbers, (self.length // 2))
            for number in range( 0 , self.number_of_numbers + 1):
                num = random.randint(0,10)
                password_list.append(str(num))

        #letters
        for number in range(0, (self.length -  self.number_of_characters - self.number_of_numbers)):
            letter = random.choice(lowercase_letters)
            if random.choice([True, False]) == True:
                letter.upper()
            password_list.append(letter)

        random.shuffle(password_list)
        delimeter = ''
        password = delimeter.join(password_list)

        return password
