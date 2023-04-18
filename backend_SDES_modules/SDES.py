"""
A simplified data encryption standard block cipher cryptographic algorithm
"""

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

KEY = '0111111101'


#permute
def permutate(original, fixed_key):
    new = ''
    for i in fixed_key:
        new += original[i - 1]
    return new

#the returns the left half of the bits(either 4 or 5)
def left_half(bits):
    return bits[:int(len(bits)/2)]

#the returns the right half of the bits(either 4 or 5)
def right_half(bits):
    return bits[int(len(bits)/2):]


#shifts the bits
def shift(bits):
    rotated_left_half = left_half(bits)[1:] + left_half(bits)[0]
    rotated_right_half = right_half(bits)[1:] + right_half(bits)[0]
    return rotated_left_half + rotated_right_half

#abstraction
def key1():
    return permutate(shift(permutate(KEY, FIXED_P10)), FIXED_P8)


def key2():
    return permutate(shift(shift(shift(permutate(KEY, FIXED_P10)))), FIXED_P8)


def xor(bits, key):
    new = ''
    for bit, key_bit in zip(bits, key):
        new += str(((int(bit) + int(key_bit)) % 2))
    return new


def lookup_in_sbox(bits, sbox):
    row = int(bits[0] + bits[3], 2)
    col = int(bits[1] + bits[2], 2)
    return '{0:02b}'.format(sbox[row][col])


def f_k(bits, key):
    L = left_half(bits)
    R = right_half(bits)
    bits = permutate(R, FIXED_EP)
    bits = xor(bits, key)
    bits = lookup_in_sbox(left_half(bits), S0) + lookup_in_sbox(right_half(bits), S1)
    bits = permutate(bits, FIXED_P4)
    return xor(bits, L)


def encrypt(plain_text):
    bits = permutate(plain_text, FIXED_IP)
    temp = f_k(bits, key1())
    bits = right_half(bits) + temp
    bits = f_k(bits, key2())
    print(permutate(bits + temp, FIXED_IP_INVERSE))


def decrypt(cipher_text):
    bits = permutate(cipher_text, FIXED_IP)
    temp = f_k(bits, key2())
    bits = right_half(bits) + temp
    bits = f_k(bits, key1())
    print (permutate(bits + temp, FIXED_IP_INVERSE))

if __name__ == "__main__":

    #Example encryption and decryption of an 8 bit binary string
    encrypt('11101010')
    decrypt('10100010')


#issues with all this code
'''
#!/usr/bin/env sage -python
from mpmath.libmp import sage
from sage.all import Crypto
'''

'''
sdes = SimplifiedDES()
sdes
'''



'''
import random as rnd
from utils import rotate, shuffle_by_list, bits_to_int, normalize_byte, split_bits_to_bytes, list_chunks

KEY_BITS = 10
ROUND_KEY_BITS = 8
ROUND_KEY_COUNT = 2
BLOCK_BITS = 8


def _generate_round_subkeys(key: str):
    p10 = shuffle_by_list(key, (2, 4, 1, 6, 3, 9, 0, 8, 7, 5))
    p10_half1 = p10[:len(p10) // 2]
    p10_half2 = p10[len(p10) // 2:]

    p10_half1_1 = rotate(p10_half1, -1)
    p10_half2_1 = rotate(p10_half2, -1)
    p10_half1_2 = rotate(p10_half1_1, -2)
    p10_half2_2 = rotate(p10_half2_1, -2)

    k1 = shuffle_by_list(p10_half1_1 + p10_half2_1, (5, 2, 6, 3, 7, 4, 9, 8))
    k2 = shuffle_by_list(p10_half1_2 + p10_half2_2, (5, 2, 6, 3, 7, 4, 9, 8))

    return (k1, k2)


def _s(bits_4: list, s_matrix: list[list[int]]):
    row = bits_to_int([bits_4[0], bits_4[3]])
    column = bits_to_int([bits_4[1], bits_4[2]])

    return normalize_byte(bin(s_matrix[row][column])[2:])[6:]


def _round_function(bits_4_1: list, bits_4_2: list, round_subkey: list) -> list:
    extended_to_8_bits = shuffle_by_list(bits_4_2, (3, 0, 1, 2, 1, 2, 3, 0))
    for i in range(len(extended_to_8_bits)):
        extended_to_8_bits[i] = int(extended_to_8_bits[i]) ^ int(round_subkey[i])
    extended_to_8_bits = list_chunks(extended_to_8_bits, len(extended_to_8_bits) // 2)

    p_left = extended_to_8_bits[0]
    p_right = extended_to_8_bits[1]

    p_left = _s(
        p_left,
        s_matrix=[
            [1, 0, 3, 2],
            [3, 2, 1, 0],
            [0, 2, 1, 3],
            [3, 1, 3, 1],
        ]
    )
    p_right = _s(
        p_right,
        s_matrix=[
            [1, 1, 2, 3],
            [2, 0, 1, 3],
            [3, 0, 1, 0],
            [2, 1, 0, 3],
        ]
    )

    p4 = shuffle_by_list(p_left + p_right, (1, 3, 2, 0))

    return [int(bits_4_1[i]) ^ int(p4[i]) for i in range(len(bits_4_1))]


def s_des_block_encrypt(text: str, key: str, encoding: str, *args, **kwargs) -> bytearray:
    k1, k2 = _generate_round_subkeys(key)
    encrypted_bytes = bytearray()

    for byte in bytearray(text, encoding):
        byte = bin(byte)[2:]  # get bits array without 0b
        byte = normalize_byte(byte)

        byte = shuffle_by_list(byte, (1, 5, 2, 0, 3, 7, 4, 6))  # IP^1
        byte = list_chunks(byte, len(byte) // 2)

        left_4_bits = byte[0]
        right_4_bits = byte[1]

        left_4_bits = _round_function(left_4_bits, right_4_bits, k1)
        right_4_bits = _round_function(right_4_bits, left_4_bits, k2)

        encrypted_bytes += bytearray(shuffle_by_list(right_4_bits + left_4_bits, (3, 0, 2, 4, 6, 1, 7, 5)))  # IP^-1

    return split_bits_to_bytes(encrypted_bytes)


def s_des_block_decrypt(text: str, key: str, encoding: str, *args, **kwargs) -> str:
    k1, k2 = _generate_round_subkeys(key)
    decrypted_bytes = bytearray()

    for byte in bytearray(text):
        byte = bin(byte)[2:]  # get bits array without 0b
        byte = normalize_byte(byte)

        byte = shuffle_by_list(byte, (1, 5, 2, 0, 3, 7, 4, 6))
        byte = list_chunks(byte, len(byte) // 2)

        left_4_bits = byte[0]
        right_4_bits = byte[1]

        left_4_bits = _round_function(left_4_bits, right_4_bits, k2)
        right_4_bits = _round_function(right_4_bits, left_4_bits, k1)

        decrypted_bytes += bytearray(shuffle_by_list(right_4_bits + left_4_bits, (3, 0, 2, 4, 6, 1, 7, 5)))

    return split_bits_to_bytes(decrypted_bytes).decode(encoding)


def s_des_block_generate_key(*args, **kwargs) -> str:
    return ''.join([str(rnd.randint(0, 1)) for i in range(KEY_BITS)])


s_des_block_settings = {
    'encrypt_binary_output': True,
    'decrypt_binary_input': True,
}
'''