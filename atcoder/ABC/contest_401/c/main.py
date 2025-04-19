N,K = map(int, input().split())
numbers = [0 for _ in range(N + 1)]
for i in range(N+1):
	if i < K:
		numbers[i] = 1
	elif i == K:
		numbers[i] = i
	else:
		numbers[i] = ((2 * numbers[i-1]) - numbers[i-K-1]) % (10**9)
print(numbers[N])