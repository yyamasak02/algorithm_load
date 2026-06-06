def count_pairs(b, k):
    n = len(b)
    r1, r2, res = 0, 0, 0
    for l in range(n - 1):
        r1 = max(r1, l + 1)
        r2 = max(r2, l + 1)
        while r1 < n and b[r1] - b[l] < k:
            r1 += 1
        while r2 < n and b[r2] - b[l] <= k:
            r2 += 1
        res += r2 - r1
    return res


def main():
    H, W, K = map(int, input().split())
    fields = [input() for _ in range(H)]

    # 列方向の累積和: col_sum[i][j] = 0行目からi行目までのj列の1の個数
    col_sum = [[0] * W for _ in range(H + 1)]
    for i in range(H):
        for j in range(W):
            col_sum[i + 1][j] = col_sum[i][j] + (1 if fields[i][j] == "1" else 0)

    result_count = 0
    for u in range(H):
        for d in range(u, H):
            # u行目からd行目の列ごとの和 A、その前置和 B
            b = [0] * (W + 1)
            for j in range(W):
                a_j = col_sum[d + 1][j] - col_sum[u][j]
                b[j + 1] = b[j] + a_j
            result_count += count_pairs(b, K)

    print(result_count)


if __name__ == "__main__":
    main()
