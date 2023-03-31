# user: Mousa-mahmood-hilal
#Problem: codeforces 4B - Before an Exam
d,s=map(int,input().split())
a=[[*map(int,input().split())]for _ in[0]*d]
b,c=sum(x[0]for x in a),sum(x[1]for x in a)
if b<=s<=c:
  print('YES')
  v=s-b
  r=[]
  for x,y in a:
    if v>0:
      l=min(v,y-x)
      v-=l
      x+=l
    r+=[x]
  print(*r)
else:print('NO')