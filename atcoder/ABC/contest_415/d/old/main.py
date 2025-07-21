n, m = map(int, input().split())
a = []
b = []
bottle = n
empty = 0
seals = 0
empty += bottle
bottle = 0
for _ in range(m):
    aa, bb = map(int, input().split())
    a.append(aa)
    b.append(bb)
options = sorted(
    [(a[i], b[i], a[i] - b[i]) for i in range(m)], key=lambda x: (x[2], x[0])
)
for ai, bi, _ in options:
    if empty < ai:
        continue
    transfer_num = 1 + (empty - ai) // (ai - bi)
    empty -= transfer_num * ai
    bottle += transfer_num * bi
    seals += transfer_num
    empty += bottle
    bottle = 0
print(seals)
