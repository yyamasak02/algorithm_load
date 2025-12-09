def main():
    n, x, y = map(int, input().split())
    a = sorted(list(map(int, input().split())), reverse=True)
    b = sorted(list(map(int, input().split())), reverse=True)
    ia, ib = x, y
    ra, rb = 2 * 10**5, 2 * 10**5
    for i in range(n):
        if ia - a[i] < 0:
            ra = min(ra, i)
        if ib - b[i] < 0:
            rb = min(rb, i)
        ia -= a[i]
        ib -= b[i]
    print(min(ra, rb, n - 1) + 1)
    return


if __name__ == "__main__":
    main()
