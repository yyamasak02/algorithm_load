import sys
import math


def dist2(ax, ay, bx, by):
    return (ax - bx) ** 2 + (ay - by) ** 2


def min_distance(tsx, tsy, tgx, tgy, asx, asy, agx, agy):
    tx, ty = tgx - tsx, tgy - tsy
    ta_len = math.hypot(tx, ty)
    ax, ay = agx - asx, agy - asy
    aa_len = math.hypot(ax, ay)

    tvx, tvy = tx / ta_len, ty / ta_len
    avx, avy = ax / aa_len, ay / aa_len

    def f(t):
        Tx = tgx if t >= ta_len else tsx + tvx * t
        Ty = tgy if t >= ta_len else tsy + tvy * t
        Ax = agx if t >= aa_len else asx + avx * t
        Ay = agy if t >= aa_len else asy + avy * t
        return dist2(Tx, Ty, Ax, Ay)

    Tstop = ta_len
    Astop = aa_len

    def min_in_range(l, r):
        sx, sy = tsx - asx, tsy - asy
        vx, vy = tvx - avx, tvy - avy
        if l >= Tstop:
            vx, vy = -avx, -avy
            sx, sy = tgx - asx, tgy - asy
        elif l >= Astop:
            vx, vy = tvx, tvy
            sx, sy = tsx - agx, tsy - agy

        a = vx * vx + vy * vy
        b = 2 * (sx * vx + sy * vy)
        c = sx * sx + sy * sy

        if a == 0:
            candidates = [l, r]
        else:
            t_star = -b / (2 * a)
            candidates = [l, r]
            if l <= t_star <= r:
                candidates.append(t_star)

        return min(f(t) for t in candidates)

    res2 = min_in_range(0, min(Tstop, Astop))
    if Tstop < Astop:
        res2 = min(res2, min_in_range(Tstop, Astop))
    elif Astop < Tstop:
        res2 = min(res2, min_in_range(Astop, Tstop))
    res2 = min(res2, f(max(Tstop, Astop)))

    return math.sqrt(res2)


def main():
    input = sys.stdin.readline
    T = int(input())
    for _ in range(T):
        tsx, tsy, tgx, tgy = map(int, input().split())
        asx, asy, agx, agy = map(int, input().split())
        ans = min_distance(tsx, tsy, tgx, tgy, asx, asy, agx, agy)
        print(f"{ans:.15f}")


if __name__ == "__main__":
    main()
