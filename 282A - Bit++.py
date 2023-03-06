# user: Mousa-mahmood-hilal
#Problem: codeforces 282A - Bit++
num=int(input())
c=0
for index in range(num):
    s=input()
    if s[0]=='+' or s[len(s)-1]=='+':
        c+=1
    else:
        c-=1
print(c)