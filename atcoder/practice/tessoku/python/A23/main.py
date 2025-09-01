def main():
    n, m = map(int, input().split())
    bits = 2 ** (n)
    dp = [[float("inf")] * (bits) for i in range(m + 1)]
    # pprint(dp)
    bits_array: list[int] = []
    for i in range(m):
        a = list(map(int, input().split()))
        v = 0
        for j in range(n):
            v += (2**j) * a[j]
        dp[i + 1][v] = 1
        for j in range(bits):
            if dp[i][j] != float("inf"):
                dp[i + 1][j] = min(dp[i + 1][j], dp[i][j])
                index = j | v
                dp[i + 1][index] = min(dp[i + 1][index], dp[i][j] + 1)
    print(dp[-1][-1] if dp[-1][-1] != float("inf") else -1)


if __name__ == "__main__":
    main()
