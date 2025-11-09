from bisect import bisect_left


def main():
    a_count: list[int] = [0]
    b_count: list[int] = [0]
    n, a, b = map(int, input().split())
    s: str = input()
    for c in s:
        is_a = True if c == "a" else False
        is_b = not is_a
        a_count.append(a_count[-1] + is_a)
        b_count.append(b_count[-1] + is_b)
    # pprint(a_count)
    # pprint(b_count)
    ans = 0
    for l in range(1, n + 1):
        ra = bisect_left(a=a_count, x=a + a_count[l - 1], lo=l)
        rb = bisect_left(a=b_count, x=b + b_count[l - 1], lo=l)
        if ra > n:
            continue
        ans += max(0, rb - ra)
    print(ans)
    return


if __name__ == "__main__":
    main()
