if __name__ == "__main__":
    n = int(input())
    a = []
    for _ in range(n):
        p, b, c = map(int, input().split())
        a.append((p, b, c))
    d = max(p for p, _, _ in a)
    e = d + 500 * n
    e = min(e, 10000)
    f = [0] * (e + 1)
    for g in range(e + 1):
        h = g
        for p, b, c in a:
            if p >= h:
                h += b
            else:
                h = max(0, h - c)
        f[g] = h
    q = int(input())
    for _ in range(q):
        x = int(input())
        if x <= e:
            print(f[x])
        else:
            h = x
            i = False
            for j, (p, b, c) in enumerate(a):
                if p >= h:
                    h += b
                else:
                    h = max(0, h - c)
                if h <= e:
                    for k in range(j + 1, n):
                        p2, b2, c2 = a[k]
                        if p2 >= h:
                            h += b2
                        else:
                            h = max(0, h - c2)
                    i = True
                    break
            print(h)
