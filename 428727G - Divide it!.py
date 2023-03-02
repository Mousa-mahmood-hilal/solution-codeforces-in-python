# user: Mousa-mahmood-hilal
#Problem: codeforces 428727G - Divide it!
t=int(input())
while t:
	ans = 0
	n = int(input())
	while n != 1:
		if n%2 == 0:
			n //= 2
		elif n%3 == 0:
			n = 2*n//3
		elif n%5 == 0:
			n = 4*n//5
		else:
			ans = -1
			break
		ans += 1
	print(ans)
	t-=1