sum = 0

while True:
	num = int(input())
	if (sum + num) < 0:
		break
	else:
		print(num)
		sum += num

