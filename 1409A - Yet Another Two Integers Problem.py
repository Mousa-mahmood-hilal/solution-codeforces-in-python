# user: Mousa-mahmood-hilal
#Problem: codeforces 1409A - Yet Another Two Integers Problem
k=int(input())
while k:
    a,b=map(int,input().split())
    c=abs(a-b)
    if c%10==0:
        print(c//10)
    else:
        print((c//10)+1)
        
    k-=1