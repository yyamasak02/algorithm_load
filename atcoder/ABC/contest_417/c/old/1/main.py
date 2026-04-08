n = int(input())
a = list(map(int, input().split()))

i_d: dict[int, set] = {}
j_d: dict[int, set] = {}
for i in range(n):
    i_diff: int = a[i] + i + 1
    j_diff: int = i + 1 - a[i]
    if i_diff not in i_d:
        i_d[i_diff] = set()
    i_d[i_diff].add(i + 1)
    if j_diff not in j_d:
        j_d[j_diff] = set()
    j_d[j_diff].add(i + 1)
result: int = 0
for key, values in i_d.items():
    if key in j_d:
        result += len(values) * len(j_d[key])
print(result)
