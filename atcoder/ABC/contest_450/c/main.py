import sys

sys.setrecursionlimit(10**8)


def main():
    H, W = map(int, input().split())
    fields = [input() for _ in range(H)]
    visited = [[False] * W for _ in range(H)]

    dirs = [(1, 0), (-1, 0), (0, -1), (0, 1)]

    def dfs(cy, cx) -> bool:
        result = True
        tmp = True
        if fields[cy][cx] == "." and (
            (cy == H - 1 or cy == 0) or (cx == W - 1 or cx == 0)
        ):
            result = False
        visited[cy][cx] = True
        for dy, dx in dirs:
            if (cy + dy > H - 1 or cy + dy < 0) or (cx + dx > W - 1 or cx + dx < 0):
                continue
            if visited[cy + dy][cx + dx] is True:
                continue
            if fields[cy + dy][cx + dx] == "#":
                continue
            # print(cy + dy, cx + dx)
            if (cy + dy == H - 1 or cy + dy == 0) or (cx + dx == W - 1 or cx + dx == 0):
                result = False
            tmp = dfs(cy + dy, cx + dx)
            if tmp is False:
                result = False
        return result


cd
