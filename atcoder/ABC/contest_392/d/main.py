n = int(input())
props = []
pairs = {}
for i in range(n):
    d = {}
    query = list(map(int, input().split()))
    k = query.pop(0)
    for j in range(k):
        if query[j] not in d:
            d[query[j]] = 0
        d[query[j]] += 1
    for key, value in d.items():
        d[key] = float(value / k)
    props.append(d)
result = 0
for i in range(n - 1):
    for j in range(i + 1, n):
        tmp = 0
        for k in props[i]:
            if k in props[j]:
                tmp += props[i][k] * props[j][k]
        result = max(result, tmp)
print(result)
