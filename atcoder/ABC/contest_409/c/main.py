n, ll = map(int, input().split())
d = list(map(int, input().split()))

if ll % 3 != 0:
    print(0)
    exit()
circle = [0 for i in range(ll + 1)]
circle[0] += 1
prev = 0
for i in range(n - 1):
    circle[(prev + d[i]) % ll] += 1
    prev = (prev + d[i]) % ll

ans = 0
for i in range(ll // 3):
    a, b, c = i, i + (ll // 3), i + (2 * (ll // 3))
    ans += circle[a] * circle[b] * circle[c]
print(ans)

# print(a,b,c)
# print(circle)
