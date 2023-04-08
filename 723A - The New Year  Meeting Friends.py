# user: Mousa-mahmood-hilal
#Problem: codeforces 723A - The New Year: Meeting Friends
x,y,z=map(int,input().split())
print(max(abs(x-y),abs(x-z),abs(y-z)))