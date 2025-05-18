from collections import defaultdict



if __name__ == "__main__":
    H, W, N = map(int, input().split())
    picked: list[bool] = [False] * N
    called_row: list[bool] = [False] * H
    called_col: list[bool] = [False] * W
    rows: dict[int, list[list[int, int, bool]]] = {}
    cols: dict[int, list[list[int, int, bool]]] = {}
    for _ in range(N):
        x, y = map(int, input().split())
        x -= 1
        y -= 1
        box = [x, y, False]
        if x not in rows:
            rows[x] = []
        rows[x].append(box)
        if y not in cols:
            cols[y] = []
        cols[y].append(box)

    Q: int = int(input())
    for _ in range(Q):
        query_type, pos = map(int, input().split())
        pos -= 1
        count: int = 0
        if query_type == 1:
            if not called_row[pos] and rows.get(pos):
                called_row[pos] = True
                for box in rows[pos]:
                    if not box[2]:
                        box[2] = True
                        count += 1
            print(count)
        else:
            if not called_col[pos] and cols.get(pos):
                called_col[pos] = True
                for box in cols[pos]:
                    if not box[2]:
                        box[2] = True
                        count += 1
            print(count)
