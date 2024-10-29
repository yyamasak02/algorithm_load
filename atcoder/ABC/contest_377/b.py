# https://atcoder.jp/contests/abc377/tasks/abc377_b

columns = [True for i in range(8)]
lines = [True for i in range(8)]

for i in range(8):
    s = input()
    for j in range(8):
        if s[j] == "#":
            columns[j] = False
            lines[i] = False

available_zone = sum(columns) * sum(lines)
print(available_zone)
            
