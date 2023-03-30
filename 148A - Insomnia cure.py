# user: Mousa-mahmood-hilal
#Problem: codeforces 148A - Insomnia cure
a=list()
c=0
for i in range(4):
    t=int(input())
    a.append(t)
d=int(input())
if 1 in a:
    print(d)
else:
    
    for i in range(1,d+1):
        if i%a[0]==0 or i%a[1]==0 or i%a[2]==0 or i%a[3]==0:
            c+=1
    print(c)