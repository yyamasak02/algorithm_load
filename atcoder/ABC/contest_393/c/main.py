n, m = map(int, input().split())
ans = set()
counter = 0
for i in range(m):
    u, v = map(int, input().split())
    if u < v:
        u, v = v, u
    if u != v:
        ans.add((u, v))
    counter += 1
print(counter - len(ans))
