from typing import List
from random import randint


#These method works around overflow of large integers (for some programming languages)

#Implement a function that takes an array representing an integer, D, and outputs the array D+1
def addOne(num:List[int]):
    #Consider the first digit
    if num[-1] == 9:
        num[-1]=0
        carry = 1
        if len(num)==1:
            num.insert(0,1)
            return
    else:
        carry = 0
        num[-1]+=1
        return

    #Start with the second least significant digit
    for i in range(len(num)-2,-1,-1):
        if carry:
            num[i] += 1
            if num[i] > 9:
                carry = 1
                num[i] = 0
            else:
                carry = 0
        else:
            return

#Implement a function that multiplies two array reprenseting integers
def multiplyIntArray(num1:List[int],num2:List[int])->List[int]:
    result = [0]*(len(num1)+len(num2))
    sign = -1 if (num1[0] < 0 ^ num2[0] < 0) else 1
    num1[0], num2[0] = abs(num1[0]),abs(num2[0])

    #perform simple long multiplication
    for i in range(len(num2)-1,-1,-1):
        for j in range(len(num1)-1,-1,-1):
            result[i+j+1] += num2[i]*num1[j]
            result[i+j] += result[i+j+1]//10
            result[i + j + 1] = result[i+j+1] % 10

    #Get rid of any initial zeros.
    result = result[next((idx for idx,digit in enumerate(result) if digit!=0),len(result)):] or [0]
    return [sign*result[0]] + result[1:]

if __name__ == '__main__':
    a = [9,2,3]
    b = [0]

    print(multiplyIntArray(a,b))
