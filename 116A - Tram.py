# user: Mousa-mahmood-hilal
#Problem: codeforces 116A - Tram
n=int(input())
mx=0
s=0
for i in range(n):
    x,y=map(int,input().split())
    s+=y-x
    if mx<s:
        mx=s
print(mx)
