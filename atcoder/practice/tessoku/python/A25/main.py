def main():
    dirs: list[tuple] = [(1, 0), (0, 1)]
    h, w = map(int, input().split())
    strings: list[str] = []
    for i in range(h):
        s: str = input()
        strings.append(s)
    dp: list[list[int]] = [[0 for _ in range(w)] for _ in range(h)]
    dp[0][0] = 1
    for i in range(h):
        for j in range(w):
            for dir in dirs:
                dy = i + dir[1]
                dx = j + dir[0]
                if dy >= h or dx >= w:
                    continue
                if strings[dy][dx] == ".":
                    dp[dy][dx] += dp[i][j]
    print(dp[-1][-1])

    # pass


if __name__ == "__main__":
    main()
