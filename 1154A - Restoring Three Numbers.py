# user: Mousa-mahmood-hilal
#Problem: codeforces 1154A - Restoring Three Numbers
mylist=list(map(int,input().split()))
mylist=sorted(mylist)
b=(-mylist[1]+mylist[2]+mylist[0])//2
a=mylist[0]-b
c=mylist[1]-a
print(a,b,c)