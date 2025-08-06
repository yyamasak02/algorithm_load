if __name__ == "__main__":
    s: str = input()
    t: str = input()
    len_s: int = len(s)
    len_t: int = len(t)
    dp: list[list[int]] = [[0 for i in range(len_s + 1)] for j in range(len_t + 1)]
    for y in range(1, len_t + 1):
        for x in range(1, len_s + 1):
            if s[x - 1] == t[y - 1]:
                dp[y][x] = max(dp[y - 1][x - 1] + 1, dp[y - 1][x], dp[y][x - 1])
            else:
                dp[y][x] = max(dp[y - 1][x], dp[y][x - 1])
    print(max(dp[len_t]))
