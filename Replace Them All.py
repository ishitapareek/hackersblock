num = int(input())

power = 0

temp = num

new = 0

if (num == 0):
	print(5)

else:
	while (temp > 0):
		# print(temp)
		if temp % 10 == 0:
			# print (temp % 10)
			new += 5 * (10 ** power)
		else:
			new += (temp % 10) * (10 ** power)
		# print('new',new)	

		power += 1
		temp //= 10

	print(new)		
