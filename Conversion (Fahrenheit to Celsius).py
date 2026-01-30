minF = int(input())
maxF = int(input())

step = int(input())

for f in range (minF, maxF + 1, step):
	c = int ((5/9) * (f - 32))

	print(f, c)