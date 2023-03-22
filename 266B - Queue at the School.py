# user: Mousa-mahmood-hilal
#Problem: codeforces 266B - Queue at the School
m,n=map(int,input().split())
s=input()
while n:
    s=s.replace('BG','GB')
    n-=1
print(s)
