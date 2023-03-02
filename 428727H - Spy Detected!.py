# user: Mousa-mahmood-hilal
#Problem: codeforces 428727H - Spy Detected!.
for i in range(int(input())):
    b=input()
    a=input().split()
    print(a.index(min(a,key=a.count))+1)