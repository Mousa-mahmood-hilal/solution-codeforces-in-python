# user: Mousa-mahmood-hilal
#Problem: codeforces 428727O - Young Physicist
n=int(input())
x=y=z=0
for i in range(n):
    arr=list(map(int,input().split()))
    x+=arr[0]
    y+=arr[1]
    z+=arr[2]
if not x and not y and not z:
    print('YES')
else:
    print('NO')