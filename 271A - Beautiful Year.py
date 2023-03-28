# user: Mousa-mahmood-hilal
#Problem: codeforces 271A - Beautiful Year
s=input()
t=int(s)+1
s=str(t)
while True:
    a=set()
    for i in s:
        a.add(i)
    if len(a)==4:
        print(s)
        break
    else:
        t=int(s)+1
        s=str(t)