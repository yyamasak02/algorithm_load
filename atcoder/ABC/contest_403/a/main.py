N = int(input())
A = list(map(int, input().split()))

ans: int = 0
for i in range(N):
    if (i+1) % 2 == 1:
        ans += A[i]
print(ans)