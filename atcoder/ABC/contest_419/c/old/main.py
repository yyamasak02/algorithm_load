def can_meet(t, p):
    min_r = min(x for x, _ in p)
    max_r = max(x for x, _ in p)
    min_c = min(y for _, y in p)
    max_c = max(y for _, y in p)
    return max(max_r - min_r, max_c - min_c) <= 2 * t


def solve(p, n):
    if all(x == p[0] for x in p):
        return 0
    left = 0
    right = 10**9
    while right - left > 1:
        mid = (left + right) // 2
        if can_meet(mid, p):
            right = mid
        else:
            left = mid
    return right


if __name__ == "__main__":
    n = int(input())
    p = []
    for _ in range(n):
        r, c = map(int, input().split())
        p.append((r, c))
    print(solve(p, n))
