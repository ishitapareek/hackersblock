num = int(input())

isPrime = True

for i in range (2, num // 2):
	if num % i == 0:
		isPrime = False

if isPrime:
	print("Prime")

else:
	print("Not Prime")