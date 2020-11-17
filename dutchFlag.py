from typing import List
import copy
from random import randint

#Implement a quicksort partition scheme: Dutch national flag partitioning
# (prevents worst case of repeating elements)
# Given an index, sort s.t. if x<=pivot, leftsize of pivot, else right

#Trivial: O(n) space and time complexity
def dutchFlagPartTrivial(arr:List[int],pivot_idx: int)->List[int]:
    if len(arr)<=1:
        return arr
    pivot = arr[pivot_idx]
    arr.remove(pivot)
    less = []
    equal = [pivot]
    larger = []

    for x in arr:
        if x<pivot:
            less.append(x)
        elif x == pivot:
            equal.append(x)
        else:
            larger.append(x)

    return less + equal + larger

#Smarter we reduced space to O(1): O(n) time complexity
# we reduced it by switching altering the input as we iterate
def dutchFlagPartSave(arr:List[int],pivot_idx: int) -> None:
    if len(arr)<=1:
        return arr
    pivot = arr[pivot_idx]

    #initialize idx that keeps track of the subarray of smaller elements
    small_val_idx = 0
    for i in range(len(arr)):
        #if element belongs in subarray of smaller elements
        if arr[i]<pivot:
            #Swap values (this works cause python evaluates the right hand side first)
            arr[i], arr[small_val_idx] = arr[small_val_idx], arr[i]
            #increase subarray size
            small_val_idx += 1

    #initialize idx that keeps track of subarray of larger elements
    big_val_idx = len(arr)-1
    for i in range(len(arr)-1,-1,-1):
        #if we iterated into smaller subarray, we're done
        if arr[i] < pivot:
            break
        elif arr[i] > pivot:
            arr[i], arr[big_val_idx] = arr[big_val_idx], arr[i]
            big_val_idx-=1


if __name__ == '__main__':
    a = [-1,-1,-1,-1,-1]
    b = copy.deepcopy(a)
    print(dutchFlagPartTrivial(a,0))
    dutchFlagPartSave(b,0)
    print(b)