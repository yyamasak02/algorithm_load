n, m = map(int, input().split())
s = input()
t = input()
columutive_nums = [0 for _ in range(n + 2)]
c_s = ["" for i in range(n)]
for i in range(m):
    ll, r = map(int, input().split())
    columutive_nums[ll] += 1
    columutive_nums[r + 1] -= 1
ans = 0
for i in range(1, n + 1):
    ans += columutive_nums[i]
    if ans % 2 == 0:
        c_s[i - 1] = s[i - 1]
    else:
        c_s[i - 1] = t[i - 1]
# print(columutive_nums)
print("".join(c_s))
