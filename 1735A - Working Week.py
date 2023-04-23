# user: Mousa-mahmood-hilal
#Problem: codeforces 1735A - Working Week
k=int(input())
while k:
    n=int(input())
    n-=6
    if n>0:
        print(n//3)
    else:
        print(0)
    k-=1