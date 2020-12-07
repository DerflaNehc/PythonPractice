from typing import List
from random import randint


#Given an array A and a mapping array P, map the elements of A using P
#Hint: Any permutation can be thought of as a set of cyclic permutation. FOr an element in a cycle
#how would you identify it as permuted

#Brute force, O(N) time and space complexity
def permBrute(A:List[int],P:List[int])->List[int]:
    tempArr = [0]*len(A)
    for idx,val in enumerate(P):
        tempArr[val] = A[idx]
    return tempArr

#We can save storage by iteratong in the input A
#We can reduce complexity by knowing the fact that a permutation array is a collection of independent cyclic permutations
#i.e. we map i to P[i] till we get back to original
def permCyclic(A:List[int],P:List[int])->List[int]:
    n = len(P)
    for i in range(len(A)):
        next = i
        while P[next] >= 0 :
            A[i],A[P[next]] = A[P[next]], A[i]
            temp = P[next]
            P[next] -= n
            next = temp
    return A

#Given an array and subset size, return a random subset of that size (all subsets should be equally as likely)
def newSubset(A:List[int],k:int)->List[int]:
    if k<=0:
        return []
    #The save space, use the input A
    #Pick a random index, swap values and pick another random index with the remaining array
    for i in range(k):
        idx = randint(i,len(A)-1)
        A[i], A[idx] = A[idx], A[i]
    return A[:k]

#Given an int n, return a subset from {0,1,...,n-1} where each subset is equally as likely
#Brute force method (using above technique) is O(n) space and time (with O(k) to compute subset).
# WHat if k << n? we can make a O(k) space and time alggorithm using a dictionary (hash table)
def randomSubset(n:int,subset_size:int)->List[int]:
    #Assume 0<subset_size<n, n>1
    dict_subset = {}
    for i in range(subset_size):
        num = randint(i,n)
        #get the mapped keys if they exist, if not then A[i] = i
        random_idx = dict_subset.get(num,num)
        mapped_i = dict_subset.get(i,i)
        dict_subset[random_idx] = mapped_i
        dict_subset[i] = random_idx
    return [dict_subset[x] for x in range(subset_size)]


if __name__ == '__main__':
    # a = [0,1,2,3]
    # p = [1,0,3,2]
    # print(permBrute(a,p))
    # print(permCyclic(a,p))
    # print(newSubset(a,2))
    print(randomSubset(7,7))

