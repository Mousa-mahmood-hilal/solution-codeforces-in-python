# user: Mousa-mahmood-hilal
#Problem: codeforces 158A - Next Round
a,b=input().split()
x=list(map(int,input().split()))
c=0
for index in range(int(a)):
    if(x[index]!=0 and x[index]>=x[int(b)-1] ):
        c+=1
print(c)