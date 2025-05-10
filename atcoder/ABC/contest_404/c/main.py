
import sys
sys.setrecursionlimit(1 << 25)

def dfs(v, ans_graph, visited):
    visited[v] = True
    for u in ans_graph[v]:
        if not visited[u]:
            dfs(u, ans_graph, visited)

if __name__ == "__main__":
    ans_dict = {}
    n, m = map(int, input().split())
    ans_graph = [[] for _ in range(n + 1)]
    for i in range(n):
        ans_dict[i+1] = 0
    for i in range(m):
        a, b = map(int, input().split())
        ans_dict[a] += 1
        ans_dict[b] += 1
        ans_graph[a].append(b)
        ans_graph[b].append(a)
    if m != n:
        print("No")
        exit()
    for i in ans_dict:
        if ans_dict[i] != 2:
            print("No")
            exit()
    visited = [False] * (n + 1)
    dfs(1, ans_graph, visited)
    if all(visited[1:]):
        print("Yes")
    else:
        print("No")


