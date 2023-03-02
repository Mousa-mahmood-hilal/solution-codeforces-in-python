# user: Mousa-mahmood-hilal
#Problem: codeforces 428727J - Pro Bending
n,m=map(int,input().split())
arr=list(map(int,input().split()))
arr.sort()
if arr[n-1]<m:
    print('Easy Win!')
else:
    print('Difficult Loss')