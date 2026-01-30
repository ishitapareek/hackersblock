sb = int(input())
db = int(input())
sn = int(input())

dec = 0
power = 0

while sn > 0:
	digit = sn % 10
	dec += digit * (sb ** power)

	sn //= 10

	power += 1

convertedNum = 0
power = 1

while dec > 0:
	rem = dec % db

	convertedNum += rem * power
	
	power *= 10

	dec //= db

print(convertedNum)