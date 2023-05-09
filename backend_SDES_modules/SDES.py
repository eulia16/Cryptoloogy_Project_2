
class SDES:
    FIXED_IP = [2, 6, 3, 1, 4, 8, 5, 7]
    FIXED_EP = [4, 1, 2, 3, 2, 3, 4, 1]
    FIXED_IP_INVERSE = [4, 1, 3, 5, 7, 2, 8, 6]
    FIXED_P10 = [3, 5, 2, 7, 4, 10, 1, 9, 8, 6]
    FIXED_P8 = [6, 3, 7, 4, 8, 5, 10, 9]
    FIXED_P4 = [2, 4, 3, 1]

    S0 = [[1, 0, 3, 2],
          [3, 2, 1, 0],
          [0, 2, 1, 3],
          [3, 1, 3, 2]]

    S1 = [[0, 1, 2, 3],
          [2, 0, 1, 3],
          [3, 0, 1, 0],
          [2, 1, 0, 3]]

    def __init__(self, key):
        self.KEY = key

    # This function takes an original string and applies a permutation
    # specified by the fixed_key list. It returns the resulting string.
    def permutate(self, original, fixed_key):
        new = ''
        for i in fixed_key:
            new += original[i - 1]
        return new

    # This function takes a string of bits and returns the left half of
    # the bits (either 4 or 5, depending on the input).
    def left_half(self, bits):
        return bits[:int(len(bits) / 2)]

    # This function takes a string of bits and returns the right half
    # of the bits (either 4 or 5, depending on the input).
    def right_half(self, bits):
        return bits[int(len(bits) / 2):]

    # This function takes a string of bits and performs a circular shift
    # on the bits. It returns the resulting string.
    def shift(self, bits):
        rotated_left_half = self.left_half(bits)[1:] + self.left_half(bits)[0]
        rotated_right_half = self.right_half(bits)[1:] + self.right_half(bits)[0]
        return rotated_left_half + rotated_right_half

    # generates first key
    def key1(self):
        return self.permutate(self.shift(self.permutate(self.KEY, self.FIXED_P10)), self.FIXED_P8)

    # generates second key
    def key2(self):
        return self.permutate(self.shift(self.shift(self.shift(self.permutate(self.KEY, self.FIXED_P10)))), self.FIXED_P8)

    # simple XOR
    def xor(self, bits, key):
        new = ''
        for bit, key_bit in zip(bits, key):
            new += str(((int(bit) + int(key_bit)) % 2))
        return new

    # This function looks up a value in a specified S-box (substitution box) using the first two and
    # last two bits of the input string bits. It returns the resulting value as a binary string.
    def lookup_in_sbox(self, bits, sbox):
        row = int(bits[0] + bits[3], 2)
        col = int(bits[1] + bits[2], 2)
        return '{0:02b}'.format(sbox[row][col])

    # This function takes a string of bits and a subkey key and performs the main
    # encryption function of the DES algorithm. It returns the resulting encrypted string.
    def main_encryption(self, bits, key):
        L = self.left_half(bits)

        R = self.right_half(bits)

        bits = self.permutate(R, self.FIXED_EP)

        bits = self.xor(bits, key)

        bits = self.lookup_in_sbox(self.left_half(bits), self.S0) + self.lookup_in_sbox(self.right_half(bits), self.S1)

        bits = self.permutate(bits, self.FIXED_P4)

        return self.xor(bits, L)

    # This function takes an 8-bit binary string plain_text and performs
    # the DES encryption algorithm on it. It prints the resulting encrypted string.
    def encrypt(self, plain_text):
        bits = self.permutate(plain_text, self.FIXED_IP)

        temp = self.main_encryption(bits, self.key1())

        bits = self.right_half(bits) + temp

        bits = self.main_encryption(bits, self.key2())

        print(self.permutate(bits + temp, self.FIXED_IP_INVERSE))

    # This function takes an 8-bit binary string cipher_text and performs
    # the DES decryption algorithm on it. It prints the resulting decrypted string.
    def decrypt(self, cipher_text):
        bits = self.permutate(cipher_text, self.FIXED_IP)
        temp = self.main_encryption(bits, self.key2())
        bits = self.right_half(bits) + temp
        bits = self.main_encryption(bits, self.key1())
        print(self.permutate(bits + temp, self.FIXED_IP_INVERSE))

    def temp(self):
        self.encrypt('10101100')

if __name__ == "__main__":
    # Example encryption and decryption of an 8 bit binary string
    #SDES('1010101010').encrypt('11110000')
    SDES('1010101010').decrypt('01011001')

        #encrypt('10101100')

        # decrypt('10100010')

'''
A simplified data encryption standard block cipher cryptographic algorithm

from sage import *


FIXED_IP = [2, 6, 3, 1, 4, 8, 5, 7]
FIXED_EP = [4, 1, 2, 3, 2, 3, 4, 1]
FIXED_IP_INVERSE = [4, 1, 3, 5, 7, 2, 8, 6]
FIXED_P10 = [3, 5, 2, 7, 4, 10, 1, 9, 8, 6]
FIXED_P8 = [6, 3, 7, 4, 8, 5, 10, 9]
FIXED_P4 = [2, 4, 3, 1]

S0 = [[1, 0, 3, 2],
      [3, 2, 1, 0],
      [0, 2, 1, 3],
      [3, 1, 3, 2]]

S1 = [[0, 1, 2, 3],
      [2, 0, 1, 3],
      [3, 0, 1, 0],
      [2, 1, 0, 3]]


def setKey(newKey):
    KEY = newKey
    return KEY

KEY = setKey() #'0111111101' #'1010101010' #'0111111101'




#This function takes an original string and applies a permutation
#specified by the fixed_key list. It returns the resulting string.
def permutate(original, fixed_key):
    new = ''
    for i in fixed_key:
        new += original[i - 1]
    return new

#This function takes a string of bits and returns the left half of
#the bits (either 4 or 5, depending on the input).
def left_half(bits):
    return bits[:int(len(bits)/2)]

# This function takes a string of bits and returns the right half
#of the bits (either 4 or 5, depending on the input).
def right_half(bits):
    return bits[int(len(bits)/2):]


#This function takes a string of bits and performs a circular shift
#on the bits. It returns the resulting string.
def shift(bits):
    rotated_left_half = left_half(bits)[1:] + left_half(bits)[0]
    rotated_right_half = right_half(bits)[1:] + right_half(bits)[0]
    return rotated_left_half + rotated_right_half

#generates first key
def key1():
    return permutate(shift(permutate(KEY, FIXED_P10)), FIXED_P8)

#generates second key
def key2():
    return permutate(shift(shift(shift(permutate(KEY, FIXED_P10)))), FIXED_P8)

#simple XOR
def xor(bits, key):
    new = ''
    for bit, key_bit in zip(bits, key):
        new += str(((int(bit) + int(key_bit)) % 2))
    return new

#This function looks up a value in a specified S-box (substitution box) using the first two and
#last two bits of the input string bits. It returns the resulting value as a binary string.
def lookup_in_sbox(bits, sbox):
    row = int(bits[0] + bits[3], 2)
    col = int(bits[1] + bits[2], 2)
    return '{0:02b}'.format(sbox[row][col])

#This function takes a string of bits and a subkey key and performs the main
#encryption function of the DES algorithm. It returns the resulting encrypted string.
def main_encryption(bits, key):
    L = left_half(bits)

    R = right_half(bits)

    bits = permutate(R, FIXED_EP)

    bits = xor(bits, key)

    bits = lookup_in_sbox(left_half(bits), S0) + lookup_in_sbox(right_half(bits), S1)

    bits = permutate(bits, FIXED_P4)

    return xor(bits, L)

#This function takes an 8-bit binary string plain_text and performs
#the DES encryption algorithm on it. It prints the resulting encrypted string.
def encrypt(plain_text):
    bits = permutate(plain_text, FIXED_IP)

    temp = main_encryption(bits, key1())

    bits = right_half(bits) + temp


    bits = main_encryption(bits, key2())

    print(permutate(bits + temp, FIXED_IP_INVERSE))

#This function takes an 8-bit binary string cipher_text and performs
#the DES decryption algorithm on it. It prints the resulting decrypted string.
def decrypt(cipher_text):
    bits = permutate(cipher_text, FIXED_IP)
    temp = main_encryption(bits, key2())
    bits = right_half(bits) + temp
    bits = main_encryption(bits, key1())
    print (permutate(bits + temp, FIXED_IP_INVERSE))

if __name__ == "__main__":
    #Example encryption and decryption of an 8 bit binary string
    encrypt('10101100')

    #decrypt('10100010')
    
'''