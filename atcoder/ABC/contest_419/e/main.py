if __name__ == "__main__":
    n: int = None
    m: int = None
    ll: int = None
    a: list[int] = None

    n, m, ll = map(int, input().split())
    a = list(map(int, input().split()))
    f = [[0 for _ in range(m)] for _ in range(ll)]
    dp = [[0 for _ in range(m)] for _ in range(ll)]
    for i in range(n):
        for r in range(m):
            amari: int = a[i] % m
            if amari > r:
                amari = m - (amari - r)
            else:
                amari = r - amari
            f[i % ll][r] += amari
    INF = 10**18
    dp = [[INF] * m for _ in range(ll + 1)]
    dp[0][0] = 0
    for i in range(1, ll + 1):
        for j in range(m):
            # if dp[i-1][j] == INF:
            #     continue
            for k in range(m):
                nj = (j + k) % m
                dp[i][nj] = min(dp[i][nj], dp[i - 1][j] + f[i - 1][k])
                # print(dp[i][nj])

    print(dp[ll][0])

    # from pprint import pprint
    # pprint(f)
