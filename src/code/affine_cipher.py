#!/usr/bin/env python3

from math import gcd

class Affine():

    def __init__(self, a, b, m):
        self.a = a
        self.b = b
        self.m = m

    def coprime(self, a, b):
        return gcd(a, b) == 1

    def encrypt(self, msg):
        ciphertext = ''
        for c in msg.upper():
            tmp = (self.a * (ord(c) - ord('A')) + self.b) % self.m
            ciphertext += chr(tmp + ord('A'))
        return ciphertext
    
    def decrypt(self, ciphertext):
        if not self.coprime(self.a, self.m):
            raise ValueError('Multiplicative inverse does not exist')
        inverse = 0
        while (inverse * self.a) % self.m != 1:
            inverse += 1
        plaintext = ''
        for c in ciphertext:
            tmp = (inverse * ((ord(c) - ord('A')) - self.b)) % self.m
            plaintext += chr(tmp + ord('A'))
        return plaintext

def main():
    affine = Affine(5, 8, 26)
    print(affine.encrypt('AFFINECIPHER'))
    print(affine.decrypt('IHHWVCSWFRCP'))

if __name__ == '__main__':
    main()