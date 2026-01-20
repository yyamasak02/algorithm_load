from collections import deque


def main():
    H, W = map(int, input().split())
    fields: list[str] = [input().rstrip() for _ in range(H)]
    costs: list[int] = [
        [[float("inf") for _ in range(2)] for _ in range(W)] for _ in range(H)
    ]
    st, gt = (0, 0), (0, 0)
    for i in range(H):
        for j in range(W):
            if fields[i][j] == "S":
                st = (i, j)
            if fields[i][j] == "G":
                gt = (i, j)
    dq: deque[int, int, int] = deque()
    dq.append((*st, 0))
    costs[st[0]][st[1]][0] = 0

    dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    while dq:
        cy, cx, flag = dq.popleft()
        for dy, dx in dirs:
            if H - 1 < cy + dy or cy + dy < 0:
                continue
            if W - 1 < cx + dx or cx + dx < 0:
                continue
            if fields[cy + dy][cx + dx] == "#":
                continue
            field_element = fields[cy + dy][cx + dx]
            current_cost = (
                costs[cy][cx][(flag + 1) % 2]
                if fields[cy][cx] == "?"
                else costs[cy][cx][flag % 2]
            )
            is_smaller = current_cost + 1 < costs[cy + dy][cx + dx][flag % 2]
            if field_element in ["S", ".", "G", "?"] and is_smaller is True:
                costs[cy + dy][cx + dx][flag % 2] = current_cost + 1
                if field_element == "?":
                    dq.append((cy + dy, cx + dx, flag + 1))
                else:
                    dq.append((cy + dy, cx + dx, flag))
            elif field_element in ["o", "x"] and is_smaller is True:
                if field_element == "o" and flag % 2 == 0:
                    costs[cy + dy][cx + dx][flag % 2] = current_cost + 1
                    dq.append((cy + dy, cx + dx, flag))
                if field_element == "x" and is_smaller is True and flag % 2 == 1:
                    costs[cy + dy][cx + dx][flag % 2] = current_cost + 1
                    dq.append((cy + dy, cx + dx, flag))
    result = min(costs[gt[0]][gt[1]])
    if result == float("inf"):
        print(-1)
    else:
        print(result)
    return


if __name__ == "__main__":
    main()
