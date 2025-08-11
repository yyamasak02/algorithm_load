s = input()
n = len(s)
t = list(s)

i = 0
while i < n:
    if s[i] == "#":
        i += 1
        continue
    j = i
    while j < n and s[j] == ".":
        j += 1
    t[i] = "o"
    i = j

print("".join(t))
