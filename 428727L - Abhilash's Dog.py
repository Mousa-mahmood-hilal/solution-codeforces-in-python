# user: Mousa-mahmood-hilal
#Problem: codeforces 428727 - L.Abhilash's Dog
m=int(input())
n=int(input())
count=0;s=0
for i in range(n):
    t=int(input())
    s+=t
    if s<=m:
        count+=1
print(count)