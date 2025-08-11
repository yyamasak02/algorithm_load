if __name__ == "__main__":
    n: int = int(input())
    t: str = input()
    dp: list[list[int, int]] = [[0, 0] for _ in range(n + 1)]
    ans: int = 0

    for r in range(1, n + 1):
        if t[r - 1] == "0":
            dp[r][0] = dp[r - 1][1]
            dp[r][1] = dp[r - 1][0] + 1
        if t[r - 1] == "1":
            dp[r][0] = dp[r - 1][0] + 1
            dp[r][1] = dp[r - 1][1]

    ans = sum(dp[i][0] for i in range(n + 1))
    print(ans)
    # from pprint import pprint
    # pprint(dp)
