from collections import deque

h, w = map(int, input().split())
a = []
sx, sy, gx, gy = None, None, None, None
for i in range(h):
    s = input()
    a.append(s)
    if s.find("S") != -1:
        sx, sy = s.index("S"), i
    if s.find("G") != -1:
        gx, gy = s.index("G"), i

visited = [[[False] * 2 for _ in range(w)] for __ in range(h)]
d = deque()
d.append((sx, sy, 0, 0))
visited[sy][sx][0] = True
ans = -1
direction = [[1, 0], [-1, 0], [0, 1], [0, -1]]
while d:
    x, y, state, dist = d.popleft()
    if x == gx and y == gy:
        ans = dist
        break
    for delta in direction:
        nx = x + delta[0]
        ny = y + delta[1]
        if nx >= w or ny >= h or nx < 0 or ny < 0:
            continue
        c = a[ny][nx]
        nstate = state
        if c == "#":
            continue
        elif c == "?":
            nstate = not state
        elif c == "o" and nstate:
            continue
        elif c == "x" and not nstate:
            continue
        if visited[ny][nx][nstate] is False:
            visited[ny][nx][nstate] = True
            d.append((nx, ny, nstate, dist + 1))

print(ans)

# print(sx, sy)
# print(gx, gy)
