n, q = map(int, input().split())
a = list(map(int, input().split()))
ca = [0]
for c in a:
    ca.append(ca[-1] + c)
for c in a:
    ca.append(ca[-1] + c)
ca.pop(0)
index = 0
for _ in range(q):
    query = tuple(map(int, input().split()))
    if query[0] == 1:
        index += query[1]
        index %= n
    else:
        start = query[1] - 1 + index
        end = query[2] - 1 + index
        if start <= end:
            result = ca[end] - ca[start - 1] if start != 0 else ca[end]
            print(result)
