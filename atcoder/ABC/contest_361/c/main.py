def main():
    n, k = map(int, input().split())
    a = sorted(list(map(int, input().split())))
    v = 10**9
    for i in range(k + 1):
        v = min(v, a[n - k + i - 1] - a[i])
    print(v)
    return


if __name__ == "__main__":
    main()
