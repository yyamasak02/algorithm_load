def main():
    n = int(input())
    sa = []
    a = list(map(int, input().split()))
    result = n
    for i in range(1, n):
        sa.append(a[i] - a[i - 1])
    d = {}
    c = 0
    prev = None
    for v in sa:
        if prev is None:
            prev = v
            c = 1
            continue
        if v == prev:
            c += 1
        else:
            if c not in d:
                d[c] = 0
            d[c] += 1
            c = 1
            prev = v
    if c not in d:
        d[c] = 0
    d[c] += 1
    for key, v in d.items():
        result += (key * (key + 1) // 2) * v
    print(result)
    return


if __name__ == "__main__":
    main()
