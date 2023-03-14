# user: Mousa-mahmood-hilal
#Problem: codeforces 546A - Soldier and Bananas
k,n,w=map(int,input().split())
s=0
for i in range(w) :
    s+=(i+1)*k
print(s-n) if(s>n) else print(0)