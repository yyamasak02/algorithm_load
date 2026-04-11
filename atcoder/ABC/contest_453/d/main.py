from collections import deque


def main():
    H, W = map(int, input().split())
    dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    index_to_sig = ["D", "U", "R", "L"]

    counters = [[[False] * 4 for _ in range(W)] for _ in range(H)]
    parent = [
        [[(None, None, None) for _ in range(4)] for _ in range(W)] for _ in range(H)
    ]

    fields = [input() for _ in range(H)]
    g = None
    q = deque()

    for y in range(H):
        for x in range(W):
            if fields[y][x] == "S":
                for d in range(4):
                    counters[y][x][d] = True
                    parent[y][x][d] = (None, None, None)
                    q.append((x, y, d))
            if fields[y][x] == "G":
                g = (x, y)

    while q:
        x, y, d = q.popleft()

        if (x, y) == g:
            print("Yes")

            res = []
            cx, cy, cd = x, y, d

            while True:
                px, py, pd = parent[cy][cx][cd]
                if px is None:
                    break
                res.append(index_to_sig[cd])
                cx, cy, cd = px, py, pd

            print("".join(reversed(res)))
            return

        for nd, (dx, dy) in enumerate(dirs):
            nx, ny = x + dx, y + dy

            if not (0 <= nx < W and 0 <= ny < H):
                continue
            if counters[ny][nx][nd]:
                continue
            if fields[ny][nx] == "#":
                continue

            if fields[y][x] == "x" and d == nd:
                continue
            if fields[y][x] == "o" and d != nd:
                continue

            counters[ny][nx][nd] = True
            parent[ny][nx][nd] = (x, y, d)

            q.append((nx, ny, nd))

    print("No")


if __name__ == "__main__":
    main()
