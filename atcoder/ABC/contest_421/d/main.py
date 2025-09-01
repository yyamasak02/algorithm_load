from collections import deque

delta = {"U": (-1, 0), "D": (1, 0), "L": (0, -1), "R": (0, 1)}

rt, ct, ra, ca = map(int, input().split())
n, m, l = map(int, input().split())

t_steps = deque()
a_steps = deque()

for _ in range(m):
    ch, num = input().split()
    t_steps.append([delta[ch], int(num)])
for _ in range(l):
    ch, num = input().split()
    a_steps.append([delta[ch], int(num)])

ans = 0
t = [rt, ct]
a = [ra, ca]

while t_steps and a_steps:
    (dtr, dtc), len_t = t_steps[0]
    (dar, dac), len_a = a_steps[0]
    k = min(len_t, len_a)

    dx = t[0] - a[0]
    dy = t[1] - a[1]
    vx = dtr - dar
    vy = dtc - dac

    if vx == 0 and vy == 0:
        if dx == 0 and dy == 0:
            ans += k
    else:
        tcol = None
        ok = True
        if vx != 0:
            if (-dx) % vx != 0:
                ok = False
            else:
                tcol = -dx // vx
        if vy != 0:
            if (-dy) % vy != 0:
                ok = False
            else:
                tc2 = -dy // vy
                if tcol is None:
                    tcol = tc2
                elif tcol != tc2:
                    ok = False
        if ok and tcol is not None and 1 <= tcol <= k:
            ans += 1

    t[0] += dtr * k
    t[1] += dtc * k
    a[0] += dar * k
    a[1] += dac * k

    t_steps[0][1] -= k
    a_steps[0][1] -= k
    if t_steps[0][1] == 0:
        t_steps.popleft()
    if a_steps[0][1] == 0:
        a_steps.popleft()

print(ans)
