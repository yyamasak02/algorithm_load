if __name__ == "__main__":
    n, s = map(int, input().split())
    a = list(map(int, input().split()))
    a.insert(0, 0)
    dp = [[0 for _ in range(s + 1)] for _ in range(n + 1)]
    availables = [set() for _ in range(n + 1)]
    availables[0].add(0)
    for i in range(1, n + 1):
        avaliable_values: set = availables[i - 1]
        for v in avaliable_values:
            dp[i][v] = True
            availables[i].add(v)
            if v + a[i] <= s:
                dp[i][v + a[i]] = True
                availables[i].add(v + a[i])
    result: str = "Yes" if dp[-1][-1] is True else "No"
    print(result)
