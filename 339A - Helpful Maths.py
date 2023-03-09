# user: Mousa-mahmood-hilal
#Problem: codeforces 339A - Helpful Maths
s=input();x=sorted(s)
for index in range(len(x)):
    if x[index] != '+' and index!=len(x)-1:
        print(x[index],end='+')
print(x[len(x)-1])