# user: Mousa-mahmood-hilal
#Problem: codeforces 263A - Beautiful Matrix
my_list=[2,1,0,1,2]
for i in my_list:
    s=input()
    if"1"in s:print(i+my_list[s.find("1")//2])