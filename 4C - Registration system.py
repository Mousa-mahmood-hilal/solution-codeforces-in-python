# user: Mousa-mahmood-hilal
#Problem: codeforces 4C - Registration system
n=int(input())
dict ={}
for i in range(n):
    s= input()
    if s in dict:
        dict[s]+=1
        print(s,str(dict[s]),sep='')
    else:
        print("OK")
        dict[s]=0