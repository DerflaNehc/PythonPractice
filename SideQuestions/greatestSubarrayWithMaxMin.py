# Write a program to find the greatest maximum min for a given length subarray
#Brute force: iterates through all subarray lengths and computes mins O(n^2)
#However, theres a lot of redundant calcs
from typing import List
from collections import deque
from random import randint

#Trivial implimentation
def trivialGSMM(arr:List[int],n:int)->int:
    MM = min(arr[:n])
    for i in range(len(arr)-n+1):
        minVa = min(arr[i:i+n])
        MM = max(minVa,MM)
    return MM

#With dequeue datastruc
def deqGSMM(arr:List[int],n:int)->int:
    MM = min(arr[:n])
    dq = deque()
    #append their indices. simplifies calculations of popping elements outside of length n
    dq.append(0)
    #want to pop from right of dequeue till number being added is the bigger
    #this is b/c the bigger number being popped is no longer a min
    for i in range(len(arr)):
        if i-dq[0] == n:
            dq.popleft()
        while len(dq) and arr[dq[-1]]>=arr[i]:
            dq.pop()
        dq.append(i)
        #only update max if index i>=n
        if i>=n:
            MM = max(MM,arr[dq[0]])
    return MM
# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    for tests in range(10000):
        array = []
        for i in range(20):
            array.append(randint(1,100))
        n = randint(1,10)
        deq_res = deqGSMM(array,n)
        trivial_res = trivialGSMM(array,n)
        assert deq_res==trivial_res,\
            'deque = {}, trivial = {}, array = {}, n = {}'.format(
                deq_res, 
                trivial_res,
                array,
                n
            )