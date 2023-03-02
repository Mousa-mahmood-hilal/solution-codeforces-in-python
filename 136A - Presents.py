# user: Mousa-mahmood-hilal
#Problem: codeforces 136A - Presents
k=int(input())
a=list(map(int,input().split()))
b=a.copy()
for i in range(k):
   b[a[i]-1]=i+1
print(*b)