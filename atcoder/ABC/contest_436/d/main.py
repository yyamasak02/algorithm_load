from collections import deque
import sys


def main():
    input = sys.stdin.readline
    h, w = map(int, input().split())
    MAX_VALUE = 10**9
    fields = [input().rstrip() for _ in range(h)]
    dirs = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    avail_zone = {}
    for y in range(h):
        for x in range(w):
            if fields[y][x] != "." and fields[y][x] != "#":
                if fields[y][x] not in avail_zone:
                    avail_zone[fields[y][x]] = set()
                avail_zone[fields[y][x]].add((y, x))
    counters = [[MAX_VALUE] * w for _ in range(h)]
    # print(fields)
    d = deque()
    d.append((0, 0))
    counters[0][0] = 0
    while d:
        y, x = d.popleft()
        for dy, dx in dirs:
            if y + dy >= h or y + dy < 0:
                continue
            if x + dx >= w or x + dx < 0:
                continue
            if fields[y + dy][x + dx] == "#":
                continue
            next_step = counters[y][x] + 1
            if next_step >= counters[y + dy][x + dx]:
                continue
            d.append((y + dy, x + dx))
            counters[y + dy][x + dx] = counters[y][x] + 1
        if fields[y][x] != ".":
            next_step = counters[y][x] + 1
            for dy, dx in avail_zone[fields[y][x]]:
                if next_step >= counters[dy][dx]:
                    continue
                d.append((dy, dx))
                counters[dy][dx] = counters[y][x] + 1
            avail_zone[fields[y][x]] = set()
    # print(counters)
    if counters[h - 1][w - 1] == MAX_VALUE:
        print(-1)
    else:
        print(counters[h - 1][w - 1])
    return


if __name__ == "__main__":
    main()
