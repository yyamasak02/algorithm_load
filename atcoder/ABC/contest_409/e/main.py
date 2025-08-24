import sys

sys.setrecursionlimit(10**7)

n = int(input())
x = list(map(int, input().split()))
g: list[list[tuple[int, int]]] = [[] for _ in range(n)]

for _ in range(n - 1):
    u, v, w = map(int, input().split())
    u -= 1
    v -= 1
    g[u].append((v, w))
    g[v].append((u, w))

ans = 0


def dfs(u: int, parent: int) -> int:
    global ans
    balance = x[u]
    for v, w in g[u]:
        if v == parent:
            continue
        child_balance = dfs(v, u)
        ans += abs(child_balance) * w
        balance += child_balance
    return balance


dfs(0, -1)
print(ans)
