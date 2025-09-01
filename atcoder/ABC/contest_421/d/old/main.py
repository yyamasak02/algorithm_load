from collections import deque


def mv(ch):
    return {
        "U": (-1, 0),
        "D": (1, 0),
        "L": (0, -1),
        "R": (0, 1),
    }[ch]


def count_in_block(dr, dc, wr, wc, L):
    if wr == 0 and wc == 0:
        return L if (dr == 0 and dc == 0) else 0
    if wr == 0:
        if dr != 0:
            return 0
        if wc == 0:
            return 0
        if dc % wc != 0:
            return 0
        u = -dc // wc
        return 1 if 1 <= u <= L else 0
    if wc == 0:
        if dc != 0:
            return 0
        if dr % wr != 0:
            return 0
        u = -dr // wr
        return 1 if 1 <= u <= L else 0
    if dr % wr != 0 or dc % wc != 0:
        return 0
    u1 = -dr // wr
    u2 = -dc // wc
    return 1 if (u1 == u2 and 1 <= u1 <= L) else 0


rt, ct, ra, ca = map(int, input().split())
n, m, l = map(int, input().split())

t_steps = deque()
a_steps = deque()

for _ in range(m):
    ch, num = input().split()
    t_steps.append([mv(ch), int(num)])
for _ in range(l):
    ch, num = input().split()
    a_steps.append([mv(ch), int(num)])

dr = rt - ra
dc = ct - ca
ans = 0

while t_steps and a_steps:
    (dtr, dtc), len_t = t_steps[0]
    (dar, dac), len_a = a_steps[0]
    k = min(len_t, len_a)

    wr, wc = dtr - dar, dtc - dac
    ans += count_in_block(dr, dc, wr, wc, k)

    dr += wr * k
    dc += wc * k

    t_steps[0][1] -= k
    a_steps[0][1] -= k
    if t_steps[0][1] == 0:
        t_steps.popleft()
    if a_steps[0][1] == 0:
        a_steps.popleft()

print(ans)
