n = int(input())

for i in range (0, n):
	lic = abs(int(input()))

	oddSum = 0
	evenSum = 0

	temp = lic

	while (temp > 0):
		digit = temp % 10

		if (digit % 2 == 0):
			evenSum += digit
		
		else:
			oddSum += digit

		temp = temp // 10

	if (evenSum % 4 == 0 or oddSum % 3 == 0):
		print("Yes")
	else:
		print("No")

	

