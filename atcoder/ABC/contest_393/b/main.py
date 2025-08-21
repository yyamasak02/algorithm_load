s = input()
s_len = len(s)
result = []

for i in range(s_len - 2):
    if s[i] == "A":
        for j in range(i + 1, s_len - 1):
            if s[j] == "B":
                if j + (j - i) < s_len and s[j + j - i] == "C":
                    result.append((i, j, j + j - i))
print(len(result))
