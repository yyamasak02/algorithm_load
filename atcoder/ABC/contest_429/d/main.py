from bisect import bisect_left


def main():
    n, m, c = map(int, input().split())
    a = list(map(int, input().split()))
    d = {}
    for i in range(n):
        if a[i] not in d:
            d[a[i]] = 0
        d[a[i]] += 1
    loads = sorted([(key, v) for key, v in d.items()], key=lambda x: x[0])
    columutive = [0]
    for q in loads:
        columutive.append(columutive[-1] + q[1])
    columutive.pop(0)
    for q in loads:
        columutive.append(columutive[-1] + q[1])
    # start = bisect_left(columutive, c)
    ninzu = []
    for i in range(len(loads)):
        if i != 0:
            index = bisect_left(a=columutive, x=c + columutive[i - 1], lo=i)
            # index = bisect_left(columutive[i:], c + columutive[i-1])
            ninzu.append(columutive[index] - columutive[i - 1])
        else:
            index = bisect_left(columutive, c)
            ninzu.append(columutive[index])
    ans = 0
    prev = loads[0][0]
    for i in range(1, len(loads)):
        ans += (loads[i][0] - prev) * ninzu[i]
        prev = loads[i][0]
    ans += (m - 1 - prev + loads[0][0] + 1) * ninzu[0]
    print(ans)
    return


if __name__ == "__main__":
    main()
