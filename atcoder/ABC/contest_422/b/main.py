def main():
    h, w = map(int, input().split())
    fields = [input().rstrip() for _ in range(h)]
    dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]

    def black_count(i: int, j: int):
        c = 0
        for dy, dx in dirs:
            ddy = i + dy
            ddx = j + dx
            if ddy > h - 1 or ddy < 0:
                continue
            if ddx > w - 1 or ddx < 0:
                continue
            if fields[ddy][ddx] == "#":
                c += 1
        return c == 2 or c == 4

    error = False
    for i in range(h):
        for j in range(w):
            if fields[i][j] == "#":
                if black_count(i, j) is False:
                    error = True
                    break
    if error is True:
        print("No")
    else:
        print("Yes")
    return


if __name__ == "__main__":
    main()
