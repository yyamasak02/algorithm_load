n = int(input())
ans = 0
for i in range(1, n + 1):
    flag = 1 if i % 2 == 0 else -1
    ans += flag * (i**3)
print(ans)
