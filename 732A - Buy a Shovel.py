# user: Mousa-mahmood-hilal
#Problem: codeforces 732A - Buy a Shovel
x,y=map(int,input().split())
i=1
s=x
while s%10!=y and s%10!=0:
    s=x*i
    i+=1
print(i-1) if i>1 else print(i)