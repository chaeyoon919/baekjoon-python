num = int(input())

while True:
	if num > 89:
		print('A')
		break
	elif num < 90 and num > 79:
		print('B')
		break
	elif num < 80 and num > 69:
		print('C')
		break
	elif num < 70 and num > 59:
		print('D')
		break
	else:
		print('F')
		break
