# user: Mousa-mahmood-hilal
#Problem: codeforces 1335A - Candies and Two Sisters
n=int(input())
while n:
    x=int(input())
    h=x//2
    a=x-h
    if a>h:
        print(h)
    else:
        if h-1>=1:
            print(h-1)
        else:
            print(0)
    n-=1