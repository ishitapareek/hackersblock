def gcd(a, b):
	while (b != 0):
		a, b = b, a % b 

	return a

n1 = int(input())
n2 = int(input())

lcm = (n1 * n2) // gcd(n1, n2)
print(lcm)