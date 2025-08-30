from collections import deque

h, w = map(int, input().split())
fields = [list(input()) for _ in range(h)]
for i in range(h):
    for j in range(w):
        if fields[i][j] == "S":
            sy, sx = i, j
        if fields[i][j] == "G":
            gy, gx = i, j
visited = [[[False] * 2 for _ in range(w)] for __ in range(h)]
q = deque()
q.append((sy, sx, 0, 0))
visited[sy][sx][0] = True
ans = -1
while q:
    y, x, state, dist = q.popleft()
    if y == gy and x == gx:
        ans = dist
        break
    for d in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
        ny = y + d[0]
        nx = x + d[1]
        nstate = state
        if ny < 0 or ny >= h or nx < 0 or nx >= w:
            continue
        c = fields[ny][nx]
        if c == "#":
            continue
        if c == "?":
            if state == 0:
                nstate = 1
            else:
                nstate = 0
        elif c == "o":
            if state == 1:
                continue
        elif c == "x":
            if state == 0:
                continue
        if visited[ny][nx][nstate] is False:
            visited[ny][nx][nstate] = True
            q.append((ny, nx, nstate, dist + 1))
print(ans)
