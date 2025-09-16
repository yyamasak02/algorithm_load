n = int(input())
p = list(map(int, input().split()))
q = list(map(int, input().split()))
ll = [0 for i in range(n + 1)]
for i in range(n):
    ll[q[i]] = p[i]

ans = []
for i in range(1, n + 1):
    ans.append(q[ll[i] - 1])
print(*ans)
