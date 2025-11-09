import sys

input = sys.stdin.readline


def main() -> None:
    n = int(input())
    a: list[tuple[int, int, int]] = [tuple(map(int, input().split())) for _ in range(n)]
    totalWeight = sum(t[0] for t in a)
    limitWeight = totalWeight // 2 + 1
    # 頭の重さでDPを作成する
    dp: list[list] = [[0] * limitWeight for _ in range(n + 1)]
    for y in range(1, n + 1):
        targetParts = a[y - 1]
        dp[y][0] = dp[y - 1][0] + targetParts[2]
        for x in range(1, limitWeight):
            dp[y][x] = (
                dp[y][x - 1]
                if dp[y - 1][x] + targetParts[2] < dp[y][x - 1]
                else dp[y - 1][x] + targetParts[2]
            )
            if (
                targetParts[0] <= x
                and dp[y][x] < dp[y - 1][x - targetParts[0]] + targetParts[1]
            ):
                dp[y][x] = dp[y - 1][x - targetParts[0]] + targetParts[1]
    maxWeight = max(dp[-1])
    print(maxWeight)
    return


if __name__ == "__main__":
    main()
