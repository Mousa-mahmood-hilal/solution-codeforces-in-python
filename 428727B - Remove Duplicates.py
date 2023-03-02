# user: Mousa-mahmood-hilal
#Problem: codeforces 428727B - Remove Duplicates.
n=int(input())
arr=list(map(int,input().split()))
arr.reverse()
narr=[]
for i in range(n):
    if arr[i] not in narr:
        narr.append(arr[i])
narr.reverse()
print(len(narr))
print(*narr)