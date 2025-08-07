# 足してM以上になる組み合わせが最大になるように配置する
# Aを大きい順に並べ、Bを小さい順に並べてAの各要素に対して
# Bの中でM以上になる最小の要素を探す
from bisect import bisect_left

t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    a.sort(reverse=True)
    b.sort()
    c, idx = 0, 0
    for v in a:
        idx = bisect_left(b, m - v, idx)
        if idx < n:
            c += 1
            idx += 1
        else:
            break
    print(sum(a) + sum(b) - c * m)
