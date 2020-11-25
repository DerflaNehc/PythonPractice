#Simple bit manipulation problems
from random import randint
from math import log

#Right propagate 1s starting from the smallest 1bit 00100000 -> 00111111
def rightPropagateSmallestBit(integer_64: int) -> int:
    return integer_64 | (integer_64-1)

#Determine the x mod a power of 2 (13 = 77 mod 64)
def modPower2(integer_64: int, powerOf2:int) -> int:
    #INITIAL CHeCKS:
    #if mod is larger than integer
    if integer_64<powerOf2:
        return integer_64
    #if integer is a power of 2 itself
    elif integer_64 & (integer_64-1) == 0:
        return 0
    return integer_64 &(powerOf2-1)

#Determine the x is a power of 2
def powerOfTwo(integer_64: int) -> int:
    #Check if there is only one bit initialized
    if integer_64 & (integer_64-1) == 0 and integer_64 != 0:
        return 1
    else:
        return 0

if __name__ == '__main__':
    #Test for modpower2
    for number in range(10**5):
        power = 2**randint(1,6)
        myResult = modPower2(number,power)
        trivial_res = number%power
        assert myResult == trivial_res, \
            'modPower2: mine = {}, trivial = {}, number = {}'.format(
                myResult,
                trivial_res,
                number
            )
    #Test for powerof2
    for number in range(1,10**5):
        myResult = powerOfTwo(number)
        trivial_res = log(number,2)
        trivial_res = 1 if trivial_res.is_integer() else 0
        assert myResult == trivial_res, \
            'powerOf2 mine = {}, trivial = {}, number = {}'.format(
                myResult,
                trivial_res,
                number
            )