t = int(input())

for i in range(t):
	r, s = input().split(' ')
	answer=''
	for v in s:
		answer+=v*int(r)
	print(answer)
