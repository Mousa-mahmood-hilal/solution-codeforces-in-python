# user: Mousa-mahmood-hilal
#Problem: codeforces 428727F - Tanya and Stairways
input()
a=input().split()
l=[x for x,y in zip(a,a[1:]+['1'])if'1'==y]
print(len(l))
print(*l)