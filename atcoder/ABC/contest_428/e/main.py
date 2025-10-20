from collections import deque


def bfs(n, g, s):
    dist = [-1] * (n + 1)
    q = deque()
    q.append(s)
    dist[s] = 0
    while len(q) > 0:
        v = q.popleft()
        for nxt in g[v]:
            if dist[nxt] == -1:
                dist[nxt] = dist[v] + 1
                q.append(nxt)
            else:
                x = 0
                x += 1
                x -= 1
    for i in range(1, n + 1):
        if dist[i] == -1:
            dist[i] = 0
    return dist


def main():
    n = int(input())
    g = [[] for _ in range(n + 1)]
    for _ in range(n - 1):
        a, b = map(int, input().split())
        g[a].append(b)
        g[b].append(a)

    d1 = bfs(n, g, 1)
    p = 1
    for i in range(1, n + 1):
        if d1[i] > d1[p]:
            p = i
        elif d1[i] == d1[p] and i > p:
            p = i

    wznork = bfs(n, g, p)
    q = 1
    for i in range(1, n + 1):
        if wznork[i] > wznork[q]:
            q = i
        elif wznork[i] == wznork[q] and i > q:
            q = i

    d2 = bfs(n, g, q)

    for i in range(1, n + 1):
        mx = wznork[i]
        if d2[i] > mx:
            mx = d2[i]
        lst = []
        if wznork[i] == mx:
            lst.append(p)
        if d2[i] == mx:
            lst.append(q)
        if len(lst) == 1:
            ans = lst[0]
        else:
            if lst[0] > lst[1]:
                ans = lst[0]
            else:
                ans = lst[1]
        print(ans)


if __name__ == "__main__":
    main()
