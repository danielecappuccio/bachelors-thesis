#!/usr/bin/env python2

import string

LETTERS = string.uppercase

class Vigenere():

    def __init__(self, keyword):
        self.keyword = keyword

    def encrypt(self, data):
        return self.aux(data, mode='encrypt')

    def decrypt(self, data):
        return self.aux(data, mode='decrypt')

    def aux(self, data, mode):
        index = 0
        string = []  
        for letter in data:
            position = LETTERS.find(letter.upper())
            if position == -1:
                # symbol not found, don't encrypt it
                string.append(letter)
                continue
            if mode == 'encrypt':
                position += LETTERS.find(self.keyword[index])
            elif mode == 'decrypt':
                position -= LETTERS.find(self.keyword[index])
            else:
                raise ValueError('Unknown mode')
            position %= len(LETTERS)
            string.append(LETTERS[position])
            index = (index + 1) % len(self.keyword)
        return ''.join(string)

def main():
    vigenere = Vigenere('LEMON')
    print(vigenere.encrypt('ATTACKATDAWN'))
    print(vigenere.decrypt('LXFOPVEFRNHR'))

if __name__ == '__main__':
    main()