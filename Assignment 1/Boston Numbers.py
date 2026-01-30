num = int(input())

temp = num

numSum = 0

while (temp > 0):
	numSum += (temp % 10)
	#print(temp % 10)
	temp //= 10
	#print(temp)
	
	#print(numSum)
	

temp = num

prime = []

while (temp > 1):
	for i in range (2, int(temp ** 0.5 + 1)):

		# print(i, temp % i, div)
		if temp % i == 0:
			prime.append(i)
			temp //= i
			break
		
	else:
		prime.append(temp)
		break

primeSum = 0
for i in prime:
	temp = i

	while (temp > 0):
		primeSum += temp % 10
		temp //= 10
	

# print(prime)
# print(primeSum, numSum)

if primeSum == numSum:
	print(1)
else:
	print(0)