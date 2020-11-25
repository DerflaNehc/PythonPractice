#Calculate x^y given x and y using only bit operations

#Add any two integers using bit operations
def addInt(num1:int,num2:int)->int:
    MASK = 0xFFFFFFFF
    while num2&MASK:
        #only carry if both bits are 1
        carry = (num1&num2)<<1
        #calculate sum without carry
        num1 =  num1 ^ num2
        #incorporate carry in next iteration
        num2 = carry
    return num1&MASK if num2>0 else num1

#Multiply any POSITIV two integers using bit operations
#NOTe:this function does not handle large ints
def multiplyInt(num1:int,num2:int)-> int:
    newnum = 0
    shiftcount = 0
    while num2:
        if num2&1:
            num1<<=shiftcount
            newnum = addInt(newnum,num1)
            shiftcount = 0
        shiftcount+=1
        num2 >>= 1
    return newnum


#Calculate the exponential x^y given x and y
def exponentialInt(x:int,y:int)->int:
    #Utilize property:
    # 1. x^y = x^(y_0+..+y_n) = x^y_0*..*x^y_n
    # e.g x^8 = x^(4)x^(4)
    if y == 0:
        return 1
    res = 1
    while y:
        if y&1:
            res = multiplyInt(res,x)
        x = multiplyInt(x,x)
        y>>=1
    return res

if __name__ == '__main__':
    # Test Multiplication
    for number in range(10 ** 2):
        for y in range(10**2):
            myResult = multiplyInt(number, y)
            trivial_res = number * y
            assert myResult == trivial_res, \
                'reverseBit: mine = {}, trivial = {}, number = {}, y = {}'.format(
                    myResult,
                    trivial_res,
                    number,
                    y
                )
    # Test exponential
    for number in range(10):
        for power in range(10):
            myResult = exponentialInt(number,power)
            trivial_res = number**power
            assert myResult == trivial_res, \
                'reverseBit: mine = {}, trivial = {}, number = {}, power = {}'.format(
                    myResult,
                    trivial_res,
                    number,
                    power
                )
