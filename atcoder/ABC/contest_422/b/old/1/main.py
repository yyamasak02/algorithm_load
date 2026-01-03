def judge(h, w, fields) -> bool:
    dirs: list[tuple[int, int]] = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    for i in range(h):
        for j in range(w):
            if fields[i][j] != "#":
                continue
            count_near: int = 0
            for dx, dy in dirs:
                if i + dy < 0 or i + dy >= h:
                    continue
                if j + dx < 0 or j + dx >= w:
                    continue
                if fields[i + dy][j + dx] == "#":
                    count_near += 1
            if count_near == 0 or count_near % 2 != 0:
                # print(count_near, i, j)
                return False
    return True


if __name__ == "__main__":
    h, w = map(int, input().split())
    fields: list[str] = []
    for i in range(h):
        s: str = input()
        fields.append(s)
    print("Yes" if judge(h, w, fields) is True else "No")
