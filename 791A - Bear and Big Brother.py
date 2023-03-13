# user: Mousa-mahmood-hilal
#Problem: codeforces 791A - Bear and Big Brother
l,b=map(int,input().split())
c=0
while l<=b:
    l*=3
    b*=2
    c+=1
print(c)