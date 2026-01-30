n = int(input())

odd = 0
even = 0

position = 1

while n > 0:
	digit = n % 10
	if position % 2 == 0:
		odd += digit
	
	else:
		even += digit
	
	n //= 10

	position += 1

print(even)
print(odd)
