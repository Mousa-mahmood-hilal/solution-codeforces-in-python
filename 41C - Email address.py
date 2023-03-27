# user: Mousa-mahmood-hilal
#Problem: codeforces 41C - Email address
from dataclasses import replace
s=input()
s1=''
for i in range(len(s)):
    if i!=0 and i!=len(s)-1:
        s1+=s[i]
s1=s1.replace('at','@',1)
s1=s1.replace('dot','.')
print (s[0],s1,s[len(s)-1],sep='')