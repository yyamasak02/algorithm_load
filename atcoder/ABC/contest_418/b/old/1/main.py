s = input()
len_s = len(s)
ans = float(0)
for i in range(len_s - 1):
    for j in range(i + 1, len_s):
        if s[i] == "t" and s[j] == "t" and j - i > 1:
            t = j - i + 1
            x = s[i : j + 1].count("t")
            ans = max(ans, float((x - 2) / (t - 2)))
print(ans)
