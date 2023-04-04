# user: Mousa-mahmood-hilal
#Problem: codeforces 581A - Vasya the Hipster
x,y=map(int,input().split())
mn=min(x,y)
print(str(mn),str((x+y-2*mn)//2))