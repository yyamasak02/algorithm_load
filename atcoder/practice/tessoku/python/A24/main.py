from bisect import bisect_left


def main():
    n: int = int(input())
    a: list[int] = list(map(int, input().split()))
    minimum_values: list[int] = [10**9 for _ in range(n)]
    dp = [0 for _ in range(n)]
    result: int = 0
    for i in range(n):
        index: int = bisect_left(minimum_values, a[i])
        dp[i] = index
        minimum_values[dp[i]] = a[i]
        if dp[i] > result:
            result += 1
    print(result + 1)


if __name__ == "__main__":
    main()
