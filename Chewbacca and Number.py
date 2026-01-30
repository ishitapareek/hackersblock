n = input()

num = list(n)

for i in range(len(num)):
	digit = int(num[i])
	inv = 9 - digit

	if i == 0:
		if inv != 0 and inv < digit:
			num[i] = str(inv)
	
	else:
		if inv < digit:
			num[i] = str(inv)
	
result = ""

for j in num:
	result += j

print(result)



for i in range (len(num)):
	digit = int(num[i])
	inverted = 9 - digit

	if i == 0 and inverted == 0:
		continue
	
	if inverted < digit:
		num[i] = str(inverted)

	