n1 = int(input())
n2 = int(input())

n = 1
count = 0

while (count < n1):
	curr = 3 * n + 2
	if curr % n2 != 0:
		print(curr)
		count += 1
		
	n += 1