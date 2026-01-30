number = int(input())
key = int(input())

count = 0

if number == 0 and key == 0:
	count = 1

else:
	while number > 0:
		lastDigit = number % 10
		if lastDigit == key:
			count += 1

		number //= 10 	  	

print(count)