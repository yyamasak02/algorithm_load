# https://atcoder.jp/contests/abc377/tasks/abc377_d

N, M = map(int, input().split())
section: list = [1 for i in range(M+1)]
ans: int = 0
L, R = 0, 0

for _ in range(N):
    L, R = map(int, input().split())
    section[R] = max(section[R], L+1)

for i in range(1, M+1):
    section[i] = max(section[i], section[i-1])

for i in range(1, M+1):
    ans += i - section[i] + 1
print(ans)