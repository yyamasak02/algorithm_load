import sys

sys.setrecursionlimit(10**9)


def main():
    n, m = map(int, input().split())
    edges = [tuple(map(int, input().split())) for _ in range(m)]

    best = 10**9
    colors = [-1] * (n + 1)

    def dfs(u):
        nonlocal best
        if u > n:
            cnt = 0
            for a, b in edges:
                if colors[a] == colors[b]:
                    cnt += 1
            best = min(best, cnt)
            return
        for c in (0, 1):
            colors[u] = c
            dfs(u + 1)

    dfs(1)
    print(best)
    return


if __name__ == "__main__":
    main()
