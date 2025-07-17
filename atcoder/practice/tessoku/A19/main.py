if __name__ == "__main__":
    N, W = map(int, input().split())
    dp: list[list[int]] = [[0 for _ in range(W + 1)] for _ in range(N + 1)]
    availables = [set() for _ in range(N + 1)]
    availables[0].add(0)
    for i in range(N):
        number = i + 1
        w, v = map(int, input().split())
        for value in availables[i]:
            dp[number][value] = max(dp[i][value], dp[number][value])
            availables[number].add(value)
            if value + w <= W:
                dp[number][value + w] = max(dp[i][value] + v, dp[number][value + w])
                availables[number].add(value + w)
    print(max(dp[-1]))
