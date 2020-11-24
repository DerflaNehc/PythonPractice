from typing import List
from random import randint


#Remove duplicate elements. output how many valid elements there are,
def arrayUnique(arr:List[int])->int:
    if not arr:
        return 0

    write_idx = 1
    for i in range(1,len(arr)):
        if arr[write_idx-1]!=arr[i]:
            arr[write_idx]=arr[i]
            write_idx+=1
    return write_idx

#Find the maximum profit from a stock once given an array of prices
def stockSellOnce(A:List[int])->int:
    if len(A)<=1:
        return 0
    max_profit = 0
    min_value = float('inf')
    for x in A:
        if min_value>x:
            min_value = x
        else:
            max_profit = max(max_profit,x-min_value)
    return max_profit

#Find the maximum profit from a stock twice given an array of prices
#O(n^2) time complexity O(n) space complexity
def stockSellTwiceTrivial(A:List[int])->int:
    #This maxprofit array holds the profit made if sold at i_th date and bought/sold again after
    maxprofit = [0]*(len(A)+1)
    for i in range(1, len(A)+1):
        maxprofit[i] = stockSellOnce(A[:i]) + stockSellOnce(A[i:])
    return max(maxprofit)

#Is there a way to not  have an inner loop?
# Redundant calculations when we calculate the second half of the array (A[i:])
def stockSellTwiceSmarter(A:List[int])->int:
    #This maxprofit array holds the profit made if sold at i_th date and bought/sold again after
    max_ppd = [0]*(len(A))
    max_profit = 0
    min_price = float('inf')
    for i in range(len(A)):
        min_price = min(min_price,A[i])
        max_profit = max(max_profit,A[i] - min_price)
        max_ppd[i] = max_profit

    #Calculating the second half A[i:] is like filling the array in reverse as i increases
    max_price_seen = float('-inf')
    for i in range(len(A)-1,-1,-1):
        max_price_seen = max(max_price_seen,A[i])
        max_profit = max(max_profit,max_price_seen - A[i] + max_ppd[i])

    return max_profit
if __name__ == '__main__':
    for tests in range(10000):
        array = []
        for i in range(20):
            array.append(randint(1, 100))
        my_res = stockSellTwiceSmarter(array)
        trivial_res = stockSellTwiceTrivial(array)
        assert my_res == trivial_res, \
            'mine = {}, trivial = {}, array = {}'.format(
                deq_res,
                trivial_res,
                array            )
