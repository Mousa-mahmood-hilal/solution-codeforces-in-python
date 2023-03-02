# user: Mousa-mahmood-hilal
#Problem: codeforces 428727D - Polycarp's Pockets
n=int(input())
arr=list(map(int,input().split()))
mx=0
for i in range(n):
    c=arr.count(arr[i])
    mx=max(mx,c)
print(mx)