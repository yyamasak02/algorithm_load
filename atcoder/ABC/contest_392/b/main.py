n, m = map(int, input().split())
a = list(map(int, input().split()))
missing = [False for _ in range(n)]
for e in a:
    missing[e - 1] = True

ans = []
for i in range(n):
    if missing[i] is False:
        ans.append(i + 1)
print(len(ans))
print(*ans)
