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

if __name__ == '__main__':
   print(flipInt(-21))