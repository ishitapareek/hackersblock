n = int(input())

n1 = 0
n2 = 1
fib = 0
for i in range (2, n + 1):
	fib = (n1 + n2)

	n1 = n2
	n2 = fib

print(fib)