# user: Mousa-mahmood-hilal
#Problem: codeforces 71A -Way Too Long Words
n=int(input())
for index in range(n):
    s=str(input())
    if(len(s)<=10):
        print(s)
    else:
        print(s[0],len(s)-2,s[len(s)-1],sep='')