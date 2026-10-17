from collections import deque


def main():
    H, W, K = map(int, input().split())
    fields = [input().rstrip() for _ in range(H)]
    visited = [[False] * W for _ in range(H)]
    is_safe_cols = [False] * W
    is_safe_rows = [False] * H
    for i in range(H):
        if "#" not in fields[i]:
            is_safe_rows[i] = True
    for i in range(W):
        f = "".join([fields[j][i] for j in range(H)])
        if "#" not in f:
            is_safe_cols[i] = True
    safe_cells: deque[tuple] = deque()
    result = 0
    for i in range(H):
        for j in range(W):
            if is_safe_rows[i] is True and is_safe_cols[j] is True:
                if K != 0:
                    safe_cells.append((i, j, 0))
                result += 1
                visited[i][j] = True
    dirs = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    while safe_cells:
        # print(safe_cells)
        h, w, t = safe_cells.popleft()
        for dh, dw in dirs:
            if dh + h < 0 or H - 1 < dh + h:
                continue
            if dw + w < 0 or W - 1 < dw + w:
                continue
            if fields[dh + h][dw + w] == "#":
                continue
            if visited[dh + h][dw + w] is True:
                continue
            result += 1
            visited[dh + h][dw + w] = True
            if t + 1 < K:
                safe_cells.append((dh + h, dw + w, t + 1))
    print(result)
    return


if __name__ == "__main__":
    main()
