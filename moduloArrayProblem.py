from typing import List

#min length subarray with sum%k==0 (prefix is sum(arry[:n]))
def minlengthsb(arr:List[int],k:int)->int:
    # if prefix[end]%3==prefix[start-1]%3 then array[start,end]%3==0
    n = len(arr)
    minlen = n + 1
    dict_mod = {0:-1} #this value avoids edge cases
    current_sum = 0
    #check for every end, if prefix[end]%3==prefix[start-1]%3
    for i in range(n):
        #distributive property of modulo
        current_sum = (current_sum + arr[i])%k
        if current_sum in dict_mod:
            len_temp = i - dict_mod[current_sum]
            dict_mod[current_sum] = i
            if len_temp < minlen:
                minlen = len_temp
    return minlen

#remove fewest num in array s.t. sum_arr %3==0
def minRemoveModThreeSum(arr:List[int])->int:
    # if prefix[end]%3==prefix[start-1]%3 then array[start,end]%3==0
    target_mod = sum(arr)%3
    current_sum=0
    if target_mod == 0:
        return arr
    n = len(arr)
    #check for every end, if prefix[end]%3==prefix[start-1]%3
    for i in range(n):
        #distributive property of mod,
        current_sum = (current_sum + arr[i])%3
        #if current is the target mod, remove that value and return
        if current_sum == target_mod:
            arr.pop(i)
            return arr
    return arr

if __name__ == '__main__':
    input = [5,3,6]
    print(minRemoveModThreeSum(input))