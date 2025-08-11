def dfs(current, target, visited, path, adj):
    if current == target:
        return path[:]
    for next_vertex in adj[current]:
        if not visited[next_vertex]:
            visited[next_vertex] = True
            path.append(next_vertex)
            result = dfs(next_vertex, target, visited, path, adj)
            if result:
                return result
            path.pop()
            visited[next_vertex] = False
    return None


def solve():
    t = int(input())
    for _ in range(t):
        n, m, x, y = map(int, input().split())
        a = [[] for _ in range(n + 1)]
        edges = []
        for _ in range(m):
            u, v = map(int, input().split())
            edges.append((u, v))
        edges.sort()
        for u, v in edges:
            a[u].append(v)
            a[v].append(u)
        v = [False] * (n + 1)
        v[x] = True
        p = [x]
        r = dfs(x, y, v, p, a)
        print(" ".join(map(str, r)))


if __name__ == "__main__":
    solve()
