#key generation module
import random

class KeyGeneration:
#the first method, the user must select a 10 bit key, i will
#create an empty method as the front end will handle this user input
#must ensure it is a sequence of 1's and 0's
#example https://jhafranco.com/2012/02/10/simplified-des-implementation-in-python/
#SAGE CELL API FOR SDES WILL USE THIS INSTEAD
#https://doc.sagemath.org/html/en/reference/cryptography/sage/crypto/block_cipher/sdes.html
    def select_key(self):
        '''temp function to represent the gathering of a 10 bit value'''
        pass

    def getListOfBits(self, bits):
        '''returns a list of bits from  given integer'''
        returnValue = [int(digit) for digit in str(bits)]
        return returnValue

    def randomize_bits(self, bits):
        '''This function returns a string as it must maintain the leading zeroes and an int cannot do that'''
        #if the bits passed is not an int, to represent the bits, throw an error
        if not isinstance(bits, int):
            raise ValueError("Bits must be an integer value")
            exit(0)
        #if the bits is not 10 digits, throw value error
        if len(str(bits)) > 10 or len(str(bits)) < 10:
            raise ValueError("Bits must be of length 10")
            exit(0)

        #get list of integer values
        list_of_bits = self.getListOfBits(bits)
        #now we have the list of bits, randomize them with themselves
        random.shuffle(list_of_bits)
        s = [str(i) for i in list_of_bits]
        # join list items using join()
        randomized_bits = "".join(map(str, s))

        return randomized_bits


    #psuedo tests for functions
if __name__ == "__main__":
    bits = 1010101010
    object = KeyGeneration()
    print(f"original bits: {bits}, randomized bits: {object.randomize_bits(bits)}")







