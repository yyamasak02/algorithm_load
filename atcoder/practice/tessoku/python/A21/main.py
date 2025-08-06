if __name__ == "__main__":
    n: int = int(input())
    blocks: list[tuple[int, int]] = [(None, None)]
    for i in range(n):
        p, a = map(int, input().split())
        blocks.append((p, a))
    dp = [[0 for _ in range(n + 1)] for _ in range(n + 1)]
    for i in range(1, n):
        for j in range(n, i - 1, -1):
            target_block = blocks[i]
            target_block2 = blocks[j]
            dp[i + 1][j] = max(
                dp[i + 1][j],
                dp[i][j]
                + (
                    target_block[1]
                    if target_block[0] >= i and target_block[0] <= j
                    else 0
                ),
            )
            dp[i][j - 1] = max(
                dp[i][j - 1],
                dp[i][j]
                + (
                    target_block2[1]
                    if target_block2[0] >= i and target_block2[0] <= j
                    else 0
                ),
            )
    print(max(dp[i][i] for i in range(n + 1)))
