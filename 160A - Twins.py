# user: Mousa-mahmood-hilal
#Problem: codeforces 160A - Twins
input();
sumc=count=0
arr=sorted(map(int,input().split()))
while sumc<=sum(arr):
    sumc+=arr.pop()
    count+=1
print(count)