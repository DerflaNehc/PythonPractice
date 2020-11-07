#How many square free integers are there from 1 to n? (numbers that arent factors of squares)
from typing import List
import math
#if divisible by square, then divisible by square of a prime
#n - (how many are divisble by 2 squared,3square,.. etc
# - how many are divisible by sixsquare..etc to avoid double counting
# + how many are divisible by 15 square.. to avoid triple subtracting)
def inclusion_exclusion(n:int)->int:
    primes = [2,3,5,7,11,13,17,19,23,29] #n<=29^2
    def count(k:int,primes_used:List[int])->int:
        if k==len(primes):
            product = 1
            for p in primes_used:
                product *=p*p
            if len(primes_used)%2==0:
                return n//product
            return -(n//product)
        return count(k+1,primes_used)+count(k+1,prime_used + [primes[k]])
    return count(0,[])


def numSquares(n: int) -> int:
    if n <= 0:
        return 0
    max_square = math.floor(math.sqrt(n))
    square_arr = [x ** 2 for x in range(1, max_square + 1)]
    layer_count = 0
    layer_values = {n}
    while layer_values:
        layer_count += 1
        temp_newlayer = set()
        for layer in layer_values:
            for x in square_arr:
                if layer == x:
                    return layer_count
                if x > layer:
                    break
                else:
                    temp_newlayer.add(layer - x)
        layer_values = temp_newlayer
    return layer_count


if __name__ == '__main__':
    print(numSquares(43))
