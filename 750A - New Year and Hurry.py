# user: Mousa-mahmood-hilal
#Problem: codeforces 750A - New Year and Hurry
x,y=map(int,input().split())
y=240-y
i,t=1,5
c,k=0,5
while True:
    if k<=y:
        i+=1
        k+=t*i
        c+=1
    else:
        break
if c<x:
    print(c)
else:
    print(x)