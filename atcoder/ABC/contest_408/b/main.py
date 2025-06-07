if __name__ == "__main__":
    d: dict[int, bool] = {}
    n = int(input())
    a = list(map(int, input().split()))
    for i in range(n):
        d[a[i]] = True
    values = list(d.keys())
    values.sort()
    res = len(values)
    print(res)
    print(" ".join(map(str, values)))
