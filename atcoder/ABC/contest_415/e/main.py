from pprint import pprint

if __name__ == "__main__":
    h, w = map(int, input().split())
    a = [list(map(int, input().split())) for _ in range(h)]
    p = list(map(int, input().split()))
    dp = [[10**18] * w for _ in range(h)]
    # pprint(dp)
    dp[h - 1][w - 1] = 0
    for i in range(h - 1, -1, -1):
        for j in range(w - 1, -1, -1):
            b = p[i + j] - a[i][j]
            if i < h - 1:
                dp[i][j] = min(dp[i][j], dp[i + 1][j])
            if j < w - 1:
                dp[i][j] = min(dp[i][j], dp[i][j + 1])
            dp[i][j] += b
            dp[i][j] = max(dp[i][j], 0)
    pprint(dp[0][0])
