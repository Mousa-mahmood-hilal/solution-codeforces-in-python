# user: Mousa-mahmood-hilal
#Problem: codeforces 734A - Anton and Danik
n=int(input())
s=input()
c=s.count('A')
c1=s.count('D')
if c==c1:
    print('Friendship')
elif c>c1:
    print('Anton')
else:
    print('Danik')