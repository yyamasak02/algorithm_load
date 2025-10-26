def main():
    n = int(input())
    a = list(map(int, input().split()))
    d = {}
    for i in range(n):
        if a[i] not in d:
            d[a[i]] = 0
        d[a[i]] += 1
    ans = 0
    for key, v in d.items():
        if v >= 2:
            ans += (v * (v - 1) // 2) * (n - v)
    print(ans)
    return


if __name__ == "__main__":
    main()
