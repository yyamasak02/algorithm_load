def main():
    n = int(input())
    d = {}
    a = list(map(int, input().split()))
    w = list(map(int, input().split()))
    result = 0
    for i in range(n):
        if a[i] not in d:
            d[a[i]] = []
        d[a[i]].append(w[i])
    for key, values in d.items():
        if len(values) >= 2:
            max_v = max(values)
            is_max_get = False
            for v in values:
                if v == max_v and is_max_get is False:
                    is_max_get = True
                    continue
                result += v
    print(result)
    return


if __name__ == "__main__":
    main()
