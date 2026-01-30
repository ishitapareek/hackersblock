n = int(input())

inv = 0
position = 1

while n > 0:
	digit = n % 10
	inv += position * (10 ** (digit - 1))

	n //= 10
	position += 1

print(inv)