from sortedcontainers import SortedList


def solve(n: int, m: int, a: list[int], b: list[int]) -> int:
    a = SortedList(a)
    b.sort()
    res = 0
    for bi in b:
        need = (m - bi) % m
        idx = a.bisect_left(need)
        if idx < len(a):
            res += (a[idx] + bi) % m
            a.pop(idx)
        else:
            res += (a[0] + bi) % m
            a.pop(0)
    return res


t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    result = solve(n, m, a, b)
    print(result)
