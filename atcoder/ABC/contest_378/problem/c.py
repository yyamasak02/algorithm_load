N: int = int(input())
A: list = list(map(int, input().split()))
B: list = [-1 for i in range(N)]
numbers: dict = {}

for i in A:
    numbers[i] = -1
for i in range(N):
    B[i] = numbers[A[i]]
    numbers[A[i]] = i+1
print(*B)