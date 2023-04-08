#key generation module
import random

class KeyGeneration:
#the first method, the user must select a 10 bit key, i will
#create an empty method as the front end will handle this user input
#must ensure it is a sequence of 1's and 0's
    def select_key(self):
        pass

    def getListOfBits(bits):
        returnValue = [int(digit) for digit in str(bits)]
        return returnValue

    def randomize_bits(self, bits):
        #if the bits passed is not an int, to represent the bits, throw an error
        if not isinstance(bits, int):
            raise ValueError("Bits must be an integer value")
            exit(0)
        #if the bits is not 10 digits, throw value error
        if len(str(bits)) > 10 or len(str(bits)) < 10:
            raise ValueError("Bits must be of length 10")
            exit(0)

        print(f"bits {bits}")
        #get list of integer values
        list_of_bits = KeyGeneration.getListOfBits(bits)
        print(f"new bits {list_of_bits}")
        #now we have the list of bits, randomize them with themselves
        print(f"shuffled bits: {random.shuffle(list_of_bits)}")


        return randomized_bits




    #psuedo tests for functions
if __name__ == "__main__":
    bits = 1010101010
    object = KeyGeneration()
    print(f"original bits: {bits}, randomized bits: {object.randomize_bits(bits)}")







