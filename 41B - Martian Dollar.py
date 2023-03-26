# user: Mousa-mahmood-hilal
#Problem: codeforces 41B - Martian Dollar
x,y=map(int,input().split())
l=list(map(int,input().split()))
an=y
mx=l[-1]
for i in range(x-2,-1,-1):
    mx=max(mx,l[i])
    an=max(an,y//l[i]*mx+y%l[i])
print(an)