from collections import deque

def bfs(w, h, meiro, scores, queue, arrow):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    dir_arrow = ['v', '^', '>', '<']
    while queue:
        x, y = queue.popleft()
        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]
            if 0 <= nx < h and 0 <= ny < w:
                if meiro[nx][ny] == '.':
                    if scores[nx][ny] > scores[x][y] + 1:
                        scores[nx][ny] = scores[x][y] + 1
                        arrow[nx][ny] = dir_arrow[d]
                        queue.append((nx, ny))

h,w = map(int, input().split())
meiro = []
scores = [[10**9 for _ in range(w)] for _ in range(h)]
arrow = [['' for _ in range(w)] for _ in range(h)]

queue = deque()
for i in range(h):
    row = list(input())
    meiro.append(row)
    for j in range(w):
        arrow[i][j] = row[j]
        if row[j] == 'E':
            queue.append((i, j))
            scores[i][j] = 0
bfs(w, h, meiro, scores, queue, arrow)
for ar in arrow:
    print("".join(ar))
