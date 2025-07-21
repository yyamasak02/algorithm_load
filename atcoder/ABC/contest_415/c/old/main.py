t = int(input())
for _ in range(t):
    n = int(input())
    s = input()
    len_s = 2**n - 1
    dp = [False] * (len_s + 1)
    dp[0] = True

    for i in range(len_s + 1):
        if not dp[i]:
            continue
        for k in range(n):
            j = i | (1 << k)
            print(j)
            if j > 0 and j <= len_s and s[j - 1] == "0":
                dp[j] = True
    print("Yes" if dp[len_s] is True else "No")
