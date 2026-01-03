n, m, k = map(int, input().split())
ans = []
result = [[False] * m for _ in range(n)]
for i in range(k):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    result[a][b] = True
    if all(result[a]):
        ans.append(a + 1)
print(*ans)
