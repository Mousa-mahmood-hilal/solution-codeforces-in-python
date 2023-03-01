# user: Mousa-mahmood-hilal
#Problem: codeforces 103317A-Oseye Sort
n,s=map(str,input().split())
arr=[]
f=False
if s=='a':
    f=True

for i in range(int(n)):
    arr.append(i+1)
if  f:
    print(*arr)
else:
    arr.reverse()
    print(*arr)