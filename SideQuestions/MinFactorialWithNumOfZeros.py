# Write a program to find min factorial with n number of zeros

#gives the min factorial that have numofZeros of zeros
def numZerosFactorial(n:int)->int:

    #this function returns the number of zeros give n factorial
    def zeros(n:int)->int:
        c = 0
        #counts number of multiples of 5 which gives us the number of zeros because 2*5=10
        while n:
            c +=n//5 #floor divide by 5
            n //=5 #divide n by 5 to get higher multiples of 5 (25,125,etc) multiples of 25 give 2 zeros
        return c
    count = 0
    #Binary Search,instead of a very large right, we know that 5*n guarantees n of zeros
    left = 0
    right = 5*n
    while left<right:
        mid = left + (right-left)//2
        if zeros(mid)<n:
            left = mid +1
            mid = left + (right - left) // 2
        else:
            right = mid
            mid = left + (right - left) // 2
    return left if zeros(left)==n else None

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    for i in range(101):

        print(numZerosFactorial(i))
