from collections import deque
import sys


def inside(x: int, y: int, w: int, h: int) -> bool:
    return 0 <= x < w and 0 <= y < h


def main():
    input = sys.stdin.readline
    h, w = map(int, input().split())
    dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]

    grid = [[True if c == "#" else False for c in input().rstrip()] for _ in range(h)]
    visited = [[0] * w for _ in range(h)]
    q = deque()

    counter = 0
    for y in range(h):
        for x in range(w):
            if grid[y][x] is True:
                q.append((x, y))
                visited[y][x] = 1
                counter += 1

    while q:
        x, y = q.popleft()
        for dx, dy in dirs:
            tx, ty = x + dx, y + dy
            if not inside(tx, ty, w, h):
                continue
            if grid[ty][tx] is True:
                continue

            near = 0
            for ddx, ddy in dirs:
                nx, ny = tx + ddx, ty + ddy
                if (
                    inside(nx, ny, w, h)
                    and grid[ny][nx] is True
                    and visited[ny][nx] <= visited[y][x]
                ):
                    near += 1

            if near == 1:
                grid[ty][tx] = True
                visited[ty][tx] = visited[y][x] + 1
                q.append((tx, ty))
                counter += 1

    print(counter)


if __name__ == "__main__":
    main()
