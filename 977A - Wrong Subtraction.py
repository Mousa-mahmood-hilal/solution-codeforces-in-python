# user: Mousa-mahmood-hilal
#Problem: codeforces 977A - Wrong Subtraction
x,y=map(int,input().split())
for i in range(y):
        x=[x//10,x-1][x%10>0]
print(x)