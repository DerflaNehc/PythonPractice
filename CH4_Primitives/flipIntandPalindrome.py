import math
#Flip the given two digit integer (12 -> 21)
def flipInt(num:int)->int:
    if num//10==0:
        return num
    num_remaining = abs(num)
    new_num = 0
    while num_remaining:
        new_num *= 10
        new_num += num_remaining%10
        num_remaining //= 10
    return new_num if num>0 else -new_num

#Brute force. O(n) space and time complexity
def palindromeIntTrivial(num:int)->bool:
    if num<0:
        return False
    str_num = str(num)
    if len(str_num)<=1:
        return False
    i = 0
    j = len(str_num)-1
    while i<j:
        if str_num[i]!=str_num[j]:
            return False
        i+=1
        j-=1
    return True

#Use the flipInt function and compare. O(n) and O(n) complexity
def palindromeUseFlip(num:int)->bool:
    if num<0 or num//10==0:
        return False
    if num == flipInt(num):
        return True
    return False

#Use log to save space complexity as we will iterate on the input
#O(n) and O(1) time/space complexity, respectfully
def palindromeUseLog(num:int)->bool:
    if num<0 or num//10==0:
        return False
    while num//10:
        most_significant_digit = (10 ** math.floor(math.log(num, 10)))
        if num//most_significant_digit != num%10:
            return False
        num -= most_significant_digit*(num//most_significant_digit)
        num//=10
    return True

if __name__ == '__main__':
    # Test palindromeCheck
    for number in range(10*100):
        myResult = palindromeUseLog(number)
        myResult2 = palindromeUseFlip(number)
        trivial_res = palindromeIntTrivial(number)
        assert myResult == trivial_res, \
            'palindrome: log = {}, flip = {}, trivial = {}, number = {}'.format(
                myResult,
                myResult2,
                trivial_res,
                number
            )