#Min num of characters needed s.t. palindrome
from typing import List
#Idea: find the maximum palindromic suffix/prefix (prefix is easier)
def naive(a:str)->str:
    str = a[::-1]
    n = len(a)
    for i in range(n,-1,-1):
        if str[:i]==str[i-1::-1]:
            return(a+str[i:])

#define a rolling hash function f_forward(s) = (s_0*prime^0 + s_1*prime^1+..+s_n-1*prime^n-1)modBIGPRIMe
# f_f(s+c) = (f_f(s) + c*prime^k)modBIGPRIMe
#define a backward rolling hasfunction s.t f_back(s) = f_forward(s[::-1])
#so f_b(s) = (s_0*prime^n-1..+s_n-1*prime^0)modBIGPRIMe (where s_i = index in the alphabet)
# f_b(s+c) = (f_f(s)*p + c*prime^0)modBIGPRIMe

#if f_b == f_f then most likely a palindromic subsequence, if we choose P and p correctly. since mod P loses some info
#it is possible to have a negative pos
def rolling_hase(a:str)->str:
    p = 23
    P = 666013
    str = a[::-1]
    f_f = 0
    f_b = 0
    p_pow = 1
    max_suffix_pal = 0
    for i,c in enumerate(str):
        idx = ord(c) - ord('a') #find index in the alphabet
        f_f =(f_f + idx*(p*p_pow))%P
        f_b = (f_b*p + idx*(p))%P
        p_pow *=p
        p_pow%=P #remember our modulo distribution property saves time and space
        if f_f == f_b:
            max_suffix_pal = i
    return a+str[max_suffix_pal+1:]
if __name__ == '__main__':
    a = "12321414214"
    str = a[::-1]
    n = len(a)
    for i in range(n,-1,-1):
        if str[:i]==str[i-1::-1]:
            print(a+str[i:])
    print(a[3::-1])