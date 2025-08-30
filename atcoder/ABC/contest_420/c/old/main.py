n, q = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

ans: int = 0
for i in range(n):
    ans += min(a[i], b[i])

for i in range(q):
    c, x, v = input().split()
    x = int(x) - 1
    v = int(v)
    ans -= min(a[x], b[x])
    if c == "A":
        a[x] = v
    else:
        b[x] = v
    ans += min(a[x], b[x])
    print(ans)
