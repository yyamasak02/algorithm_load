t = int(input())
for _ in range(t):
    h, w = map(int, input().split())
    k = 1 << w
    s = [input().strip() for _ in range(h)]

    a = [[True] * k for _ in range(k)]
    for i in range(k):
        for j in range(k):
            for ii in range(w - 1):
                if ((i >> ii) & 3) == 3 and ((j >> ii) & 3) == 3:
                    a[i][j] = False
                    break

    d = [float("inf")] * k
    d[0] = 0

    for i in range(h):
        st = 0
        for j in range(w):
            if s[i][j] == "#":
                st += 1 << j

        d2 = [float("inf")] * k
        for j in range(k):
            if (j | st) == st:
                for jj in range(k):
                    if a[jj][j]:
                        d2[j] = min(d2[j], d[jj] + bin(j ^ st).count("1"))

        d = d2

    ans = min(d)
    print(ans)
