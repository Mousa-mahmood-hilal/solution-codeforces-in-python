# user: Mousa-mahmood-hilal
#Problem: codeforces 59A - Word
s=input()
c=0;c1=0
for index in range(len(s)):
    if s[index].islower():
        c+=1
print(s.lower()) if c>=len(s)-c else print(s.upper())