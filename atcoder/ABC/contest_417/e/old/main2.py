def dfs(k: int, cand: list[bool], used: list[bool], edges: list[list[int]]) -> None:
    cand[k] = True
    for next_v in edges[k]:
        if not cand[next_v] and not used[next_v]:
            dfs(next_v, cand, used, edges)


def solve(
    x: int, y: int, n: int, edges: list[list[int]], used: list[bool]
) -> list[int]:
    ans = []
    cur = x
    while cur != y:
        ans.append(cur)
        used[cur] = True
        cand = [False] * n
        dfs(y, cand, used, edges)
        nxt = n
        for next_v in edges[cur]:
            if cand[next_v]:
                nxt = min(nxt, next_v)
        cur = nxt
    ans.append(y)
    return ans


if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        n, m, x, y = map(int, input().split())
        x -= 1
        y -= 1
        edges = [[] for _ in range(n)]
        used = [False] * n
        for _ in range(m):
            u, v = map(int, input().split())
            u -= 1
            v -= 1
            edges[u].append(v)
            edges[v].append(u)
        ans = solve(x, y, n, edges, used)
        print(" ".join(str(v + 1) for v in ans))
