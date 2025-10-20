import math


def ceil_sqrt(a: int) -> int:
    if a <= 0:
        return 0
    r = math.isqrt(a - 1)
    return r + 1


def main():
    t = int(input())
    pow = [1]
    for _ in range(20):
        pow.append(pow[-1] * 10)
    for _ in range(t):
        c, d = map(int, input().split())
        smin = c + 1
        smax = c + d
        m_lo = len(str(smin))
        m_hi = len(str(smax))
        ans = 0
        for m in range(m_lo, m_hi + 1):
            lo_m = pow[m - 1]
            hi_m = pow[m] - 1
            l = max(lo_m, smin)
            r = min(hi_m, smax)
            if l > r:
                continue
            a = c * pow[m] + l
            b = c * pow[m] + r
            ans += math.isqrt(b) - ceil_sqrt(a) + 1
        print(ans)


if __name__ == "__main__":
    main()
