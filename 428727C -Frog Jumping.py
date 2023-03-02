# user: Mousa-mahmood-hilal
#Problem: codeforces 428727C -Frog Jumping
n=int(input())
while n:
    a,b,c=map(int,input().split())
    f=l=c//2
    if c%2!=0:
        f+=1
    print((f*a)-(l*b))
    n-=1