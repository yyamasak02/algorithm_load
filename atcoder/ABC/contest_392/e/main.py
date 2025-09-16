n, m = map(int, input().split())
cables: list[int] = []
for i in range(m):
    a, b = map(int, input().split())
    cables.append((a, b))
print(cables)
