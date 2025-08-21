n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
dp = [0 for i in range(n + 1)]
for i in range(n - 1):
    if i != 0 and dp[i + 1] == 0:
        continue
    dp[a[i]] = max(dp[a[i]], dp[i + 1] + 100)
    dp[b[i]] = max(dp[b[i]], dp[i + 1] + 150)
print(dp[-1])
# print(dp)
