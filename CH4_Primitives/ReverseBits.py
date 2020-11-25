#Reverse a given integer by its bits e.g 0111 -> 1110
#With a bruteforce/smarter soln
global_reverse_dict = {0:0}

#Swap the bits between two indices
def swapBit(number:int,i:int, j:int)-> int:
    #index i,j where 0 is the least significant bit. Assume i<j
    mask = 2**i | 2**j
    #The swap is only necessary when index i and j have different bits (10 or 01)
    if (number>>i &1 != number>>j &1):
        number ^= mask
    return number

#Helper function to swap the bits of a number with a given bitsize
def reverseBitsHelper(number:int,size:int)->int:
    i,j = 0, size-1
    while i<j:
        number = swapBit(number,i,j)
        i+=1
        j-=1
    return number

def reverseBitTrivial(number:int)->int:
    #take the first and last 32 bits and swap each bit using swapBit, Then swap the the two 32 bit sections
    lower_32 = number & (2**31 | (2**31-1))
    upper_32 = number >> 32
    lower_32=reverseBitsHelper(lower_32, 32)
    upper_32=reverseBitsHelper(upper_32, 32)
    return (lower_32<<32)|upper_32

def reverseBit(number:int)->int:
    #Utilize a 16bit lookup table (dictionary) but create it from scratch on startup
    #create l3,l2,l1,l0 as the most to least significant 16 bit of the 64 bit integer
    MASKBIT16 = (2**15 | (2**15-1))
    BITSIZ = 16
    l0 = number & MASKBIT16
    number >>= 16
    l1 = number & MASKBIT16
    number >>= 16
    l2 = number & MASKBIT16
    number >>= 16
    l3 = number

    newnum = 0
    for n in  [l0,l1,l2,l3]:
        newnum <<=16
        if n in global_reverse_dict:
            n = global_reverse_dict[n]
        else:
            global_reverse_dict[n] = reverseBitsHelper(n,BITSIZ)
            n = global_reverse_dict[n]
        newnum |= n
    return newnum

if __name__ == '__main__':
    # Test the smarter method against brute force
    for number in range(10**5):
        myResult = reverseBit(number)
        trivial_res = reverseBitTrivial(number)
        assert myResult == trivial_res, \
            'reverseBit: mine = {}, trivial = {}, number = {}'.format(
                myResult,
                trivial_res,
                number
            )
