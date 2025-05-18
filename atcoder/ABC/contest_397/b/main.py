import copy

s = list(input())
next_s = copy.deepcopy(s)
current = len(s)
res = 0
for i in range(len(s) - 1):
    if s[i] == s[i + 1]:
        if s[i] == "i":
            next_s.insert(i + res + 1, "o")
        else:
            next_s.insert(i + res + 1, "i")
        res += 1

if s[0] == "i" and (current + res) % 2 == 0:
    print(res)
elif s[0] == "o" and (current + res) % 2 == 0:
    print(res + 2)
elif s[0] == "i" and (current + res) % 2 == 1:
    print(res + 1)
else:
    print(res + 1)

