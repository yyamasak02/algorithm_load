import sys
from collections import deque


def main():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    h = int(input_data[0])
    w = int(input_data[1])
    s = input_data[2:]

    fields = [list(row) for row in s]
    counts = [[0] * w for _ in range(h)]
    dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]

    for i in range(h):
        for j in range(w):
            if fields[i][j] == "#":
                for dx, dy in dirs:
                    nx, ny = j + dx, i + dy
                    if 0 <= nx < w and 0 <= ny < h:
                        counts[ny][nx] += 1

    counter = 0
    d = deque()
    for i in range(h):
        for j in range(w):
            if fields[i][j] == "#":
                counter += 1
            elif counts[i][j] == 1:
                d.append((j, i))

    tmp_set = set()
    while d:
        x, y = d.popleft()
        fields[y][x] = "#"
        counter += 1

        for dx, dy in dirs:
            nx, ny = x + dx, y + dy
            if 0 <= nx < w and 0 <= ny < h:
                if fields[ny][nx] == ".":
                    counts[ny][nx] += 1
                    tmp_set.add((nx, ny))

        if len(d) == 0:
            for tx, ty in tmp_set:
                if fields[ty][tx] == "." and counts[ty][tx] == 1:
                    d.append((tx, ty))
            tmp_set = set()

    print(counter)


if __name__ == "__main__":
    main()
