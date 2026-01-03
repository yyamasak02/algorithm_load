def main():
    n, q = map(int, input().split())
    a = [1] * (n + 1)
    a[0] = 0
    min_version = 1
    for _ in range(q):
        x, y = map(int, input().split())
        tmp = 0
        for v in range(min_version, x + 1):
            tmp += a[v]
            a[v] = 0
        a[y] += tmp
        min_version = max(min_version, x + 1)
        print(tmp)
    return


if __name__ == "__main__":
    main()
