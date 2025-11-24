def main():
    n, m = map(int, input().split())
    p: dict[tuple[int, int], int] = {}
    a = sorted(list(map(int, input().split())))
    max_digits = len(str(max(a)))
    result = 0
    for c in a:
        digits = len(str(c))
        mod = c % m
        if (digits, mod) not in p:
            p[(digits, mod)] = 0
        p[(digits, mod)] += 1
    # print(p)
    for i in range(n):
        tmp = a[i]
        for digit in range(1, max_digits + 1):
            tmp *= 10
            mod = tmp % m
            if (digit, (m - mod) % m) in p:
                result += p[(digit, (m - mod) % m)]
    print(result)
    return


if __name__ == "__main__":
    main()
