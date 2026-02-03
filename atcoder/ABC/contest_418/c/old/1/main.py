from bisect import bisect_left

n, q = map(int, input().split())
a = sorted(list(map(int, input().split())))
columutive_a = [0 for _ in range(n + 1)]
for index, s_a in enumerate(a):
    columutive_a[index + 1] = columutive_a[index] + s_a
columutive_a.pop(0)
# print(columutive_a)
for i in range(q):
    b = int(input())
    position_index = bisect_left(a, b)
    if position_index >= n:
        print(-1)
        continue
    result = (
        (columutive_a[position_index - 1] if position_index > 0 else 0)
        + ((b - 1) * (n - position_index - 1))
        + b
    )
    print(result)
