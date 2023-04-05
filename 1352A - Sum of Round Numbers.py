# user: Mousa-mahmood-hilal
#Problem: codeforces 1352A - Sum of Round Numbers
from math import pow
k=int(input())
while k:
    n=input()
    x=len(n)
    s=x-n.count('0')
    print(s)
    for i in range(x):
        if n[i]!='0':
            print(int(int(n[i])*(pow(10,x-i-1))),end=' ')
    print()
    k-=1