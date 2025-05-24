s = input()
digits = len(s)
ans = 0

for i in range(digits, 0, -1):
    num = int(s[i-1])
    if (i - 1 == digits - 1):
        prev = 0
    else:
        prev = int(s[i])
    if num == 0 and prev != 0:
        ans += 10 - prev
    else:
        if num >= prev:
            ans += num - prev
        else:
            ans += (10 - prev) + num
print(ans + digits)
