from typing import List
from random import randint


#Given an int, return a list of all primes less than int
#Hint, remove all multiples of prime
def primeListBrute(a:int)->List[int]:
    if a<=2:
        return a

    pa = [2]
    pflag = 1
    for x in range(3,a+1):
        for prime in pa:
            if x%prime == 0:
                pflag = 0
                break
        if pflag:
            pa.append(x)
        pflag = 1
    return pa

#Here we remove all multiples of the prime before going to the next number
#O(n^(3/2)) time because it is dictated by the multiples of prime p (O(n/2+n/3+n/5+...))
def primeListSmart1(a:int)->List[int]:
    if a<=2:
        return a
    #This list dictates if the number (by idx) is a prime.
    prime_list = [False,False] + [True] * (a-1)
    pa = []
    for x in range(2,a+1):  
        #If number is a prime
        if prime_list[x]:
            pa.append(x)

            #Remove all multiples of that prime
            for mp in range (x,a+1,x):
                prime_list[mp] = False
    return pa

#NOTe We can improve the previous method by realizing that multiples kp (k<p, p prime)
# were removed by the property of the method (since k<p). Allowing us to remove multiples of p
#  FROM p^2 instead of p
#Storage can also be reduced by ignoring even numbers

def primeListSmart2(a:int)->List[int]:
    if a<=2:
        return a
    #Size of our prime_list have been halved (with even numbers, 0, 1) removed
    size = (a-3)//2 + 1
    #prime_list[i] represents integer 2*i + 3
    prime_list = [True] * size
    pa = [2]
    for i in range(size):
        #If number is a prime
        if prime_list[i]:
            p = 2*i + 3
            pa.append(p)
            #if p = 2*i+3, p^2 =  4i^2+12i+9. Since prime_list[i] = 2i+3
            #to get the right index x s.t. prime_list[x] = 2x+3 = p^2,
            # x = 2i^2 + 6i + 3
            #Remove all multiples of p starting from p^2
            for mp in range (2*i**2 + 6*i + 3,size,p):
                prime_list[mp] = False
    return pa
if __name__ == '__main__':
    num = 19
    print(primeListBrute(num))
    print(primeListSmart1(num))
    print(primeListSmart2(num))

    # for tests in range(10000):
    #     array = []
    #     for i in range(20):
    #         array.append(randint(1, 100))
    #     my_res = stockSellTwiceSmarter(array)
    #     trivial_res = stockSellTwiceTrivial(array)
    #     assert my_res == trivial_res, \
    #         'mine = {}, trivial = {}, array = {}'.format(
    #             deq_res,
    #             trivial_res,
    #             array            )
