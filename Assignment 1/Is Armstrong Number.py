num = abs(int(input()))

temp = num

count = 0
while (temp > 0):
	temp //= 10
	count += 1

temp = num

ans = 0
while (temp > 0):
	ans += ((temp % 10) ** count)
	temp //= 10

if ans == num:
	print("true")

else:
	print("false")	
