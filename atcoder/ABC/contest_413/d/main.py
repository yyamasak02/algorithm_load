import sys

input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    if a.count(a[0]) == n:
        print("Yes")
        continue
    p_cnt = a.count(a[0])
    n_cnt = a.count(-a[0])
    if p_cnt + n_cnt == n and min(p_cnt, n_cnt) == n // 2:
        print("Yes")
        continue
    a.sort()
    ok = True
    for i in range(n - 2):
        if a[i] * a[i + 2] != a[i + 1] * a[i + 1]:
            ok = False
            break
    if ok:
        print("Yes")
        continue
    b = sorted(a, key=lambda x: -abs(x))
    ok = True
    for i in range(n - 2):
        if b[i] * b[i + 2] != b[i + 1] * b[i + 1]:
            ok = False
            break
    print("Yes" if ok else "No")
