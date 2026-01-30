n1 = int(input())
n2 = int(input())


for i in range(n1, n2 + 1):
	temp = i
	numSum = 0	

	count = 0

	while (temp > 0):
		count += 1
		temp //= 10

	temp = i

	while(temp > 0):
		numSum += (temp % 10) ** count
		temp //= 10
	
	if numSum == i:
		print(i)
		