rounds = int(input())

for i in range(0, rounds):
	M, N = map(int, input().split())

	Aayush = 0
	Harshit = 0

	num = 1
	while True:
		if (num % 2 == 0):
			Harshit += num
			
		else:
			Aayush += num

		num += 1

		if Aayush > M:
			print("Harshit")
			break

		if Harshit > N:
			print("Aayush")
			break