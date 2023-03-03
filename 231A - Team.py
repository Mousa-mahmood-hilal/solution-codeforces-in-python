# user: Mousa-mahmood-hilal
#Problem: codeforces 231A - Team
n=int(input())
c=0
for index in range(n):
    s=0
    x,y,z=map(int,input().split())
    s+=x+y+z
    if(s>=2):
        c+=1
print(c)