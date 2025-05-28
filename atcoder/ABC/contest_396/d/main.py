from copy import copy

def dfs(paths, n, current, visited, loads):
    if current == n - 1:
        loads.append(copy(visited))
        return
    
    for next_node in range(n):
        if next_node in visited or paths[current][next_node] == -1:
            continue
        visited.append(next_node)
        dfs(paths, n, next_node, visited, loads)
        visited.pop()

if __name__ == "__main__":
    n, m = map(int, input().split())
    paths = [[-1 for _ in range(n)] for _ in range(n)]
    for _ in range(m):
        u, v, w = map(int, input().split())
        paths[u-1][v-1] = w
        paths[v-1][u-1] = w
    
    loads = []
    dfs(paths, n, 0, [0], loads)
    ans = float("inf")
    for load in loads:
        res = 0
        for i in range(len(load) - 1):
            res ^= paths[load[i]][load[i+1]]
        ans = min(ans, res)
    print(ans)