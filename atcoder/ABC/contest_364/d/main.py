from bisect import bisect_left, bisect_right


def main():
    n, q = map(int, input().split())
    a = sorted(list(map(int, input().split())))

    def is_in_range(b: int, v: int, k: int) -> bool:
        cl = bisect_left(a, b - v)
        cr = bisect_right(a, b + v)
        # print((i - cl), (cr - i))
        return cr - cl >= k

    for _ in range(q):
        b, k = map(int, input().split())
        l, r = -1, 2 * (10**10)
        while r - l > 1:
            mid = (l + r) // 2
            if is_in_range(b, mid, k):
                r = mid
            else:
                l = mid
        print(r)
    return


if __name__ == "__main__":
    main()
