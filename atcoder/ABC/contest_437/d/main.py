from bisect import bisect_right, bisect_left


def main():
    n, m = map(int, input().split())
    a = sorted(list(map(int, input().split())))
    b = sorted(list(map(int, input().split())))
    minus_count_b = [0] * m
    minus_count_a = [0] * n
    for i in range(m):
        index = bisect_left(a, b[i])
        minus_count_b[i] = index
    for i in range(n):
        index = bisect_right(b, a[i])
        minus_count_a[i] = m - index
    result = 0
    for i in range(m):
        result += minus_count_b[i] * b[i]
        result -= (n - minus_count_b[i]) * b[i]
    for i in range(n):
        result -= minus_count_a[i] * a[i]
        result += (m - minus_count_a[i]) * a[i]
    print(result % 998244353)
    return


if __name__ == "__main__":
    main()
