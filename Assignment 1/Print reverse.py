num = int(input())

revNum = ''

temp = num

while (temp != 0):
	revNum += str(temp % 10)
	temp = temp // 10

print(revNum)