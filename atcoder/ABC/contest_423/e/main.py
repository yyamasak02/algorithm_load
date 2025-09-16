n, q = map(int, input().split())
a = list(map(int, input().split()))

nizyo = [0]
ichizyo = [0]
singles = [0]
for i in range(n):
    nizyo.append(nizyo[-1] + ((i + 1) * (i + 1) * a[i]))
    ichizyo.append(ichizyo[-1] + ((i + 1) * a[i]))
    singles.append(singles[-1] + a[i])

for _ in range(q):
    li, ri = map(int, input().split())
    ans = (
        ((-li + 1) * (ri + 1) * (singles[ri] - singles[li - 1]))
        + ((li + ri) * (ichizyo[ri] - ichizyo[li - 1]))
        - (nizyo[ri] - nizyo[li - 1])
    )
    print(ans)
