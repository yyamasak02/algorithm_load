import sys
sys.setrecursionlimit(1 << 25)

def solve(zoo_idx, j, k):
    global h
    if k >= h:
        return
    if zoo_idx == a:
        if all(x >= 2 for x in j):
            h = min(h, k)
        return
    for v in (2, 1, 0): 
        next_j = j[:]
        for animal in d[zoo_idx]:
            next_j[animal] += v
        solve(zoo_idx + 1, next_j, k + v * c[zoo_idx])

if __name__ == "__main__":
    a, b = map(int, input().split())
    c = list(map(int, input().split()))
    d = [set() for _ in range(a)]

    for i in range(b):
        f = list(map(int, input().split()))
        for g in f[1:]:
            d[g - 1].add(i)

    h = float("inf")
    solve(0, [0] * b, 0)
    print(h)
