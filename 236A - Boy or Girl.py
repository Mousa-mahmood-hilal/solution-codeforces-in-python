# user: Mousa-mahmood-hilal
#Problem: codeforces 236A - Boy or Girl
s=input()
set ={set}
for i in range(len(s)):
    set.add(s[i])
print("IGNORE HIM!") if (len(set)-1)%2==1 else print("CHAT WITH HER!")