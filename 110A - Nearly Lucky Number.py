# user: Mousa-mahmood-hilal
#Problem: codeforces 110A - Nearly Lucky Number
s=input()
x=int(s.count('4'))+int(s.count('7'))
print("YES") if x==4 or x==7 else print("NO")