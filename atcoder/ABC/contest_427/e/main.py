import sys
from collections import deque


def main():
    input = sys.stdin.readline
    h, w = map(int, input().split())
    s = [input().strip() for _ in range(h)]

    trash, tr, tc = [], -1, -1
    rmin, rmax = 10**9, -(10**9)
    cmin, cmax = 10**9, -(10**9)

    for i in range(h):
        for j in range(w):
            if s[i][j] == "T":
                tr, tc = i, j
            elif s[i][j] == "#":
                trash.append((i, j))
                rmin, rmax = min(rmin, i), max(rmax, i)
                cmin, cmax = min(cmin, j), max(cmax, j)

    ban = {(tr - r, tc - c) for r, c in trash}
    dmin_r, dmax_r = -(rmax + 1), h - rmin
    dmin_c, dmax_c = -(cmax + 1), w - cmin

    def all_out(dr, dc):
        for r, c in trash:
            rr, cc = r + dr, c + dc
            if 0 <= rr < h and 0 <= cc < w:
                return False
        return True

    if all_out(0, 0):
        print(0)
        return

    dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    q = deque([(0, 0, 0, 0, 0)])
    vis = {(0, 0, 0, 0)}

    while q:
        dr, dc, sr, sc, d = q.popleft()
        for ddr, ddc in dirs:
            nr, nc = dr + ddr, dc + ddc
            nsr, nsc = sr, sc

            if not (dmin_r <= nr <= dmax_r and dmin_c <= nc <= dmax_c):
                continue

            if ddr:
                t = 1 if ddr > 0 else -1
                if sr == 0:
                    nsr = t
                elif sr != t:
                    continue
            if ddc:
                t = 1 if ddc > 0 else -1
                if sc == 0:
                    nsc = t
                elif sc != t:
                    continue

            if (nr, nc) in ban:
                continue

            if all_out(nr, nc):
                print(d + 1)
                return

            st = (nr, nc, nsr, nsc)
            if st not in vis:
                vis.add(st)
                q.append((nr, nc, nsr, nsc, d + 1))
    print(-1)


if __name__ == "__main__":
    main()
