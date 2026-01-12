from bisect import bisect_left


def main():
    n, q = map(int, input().split())
    a = sorted(list(map(int, input().split())))
    # print(a)
    for _ in range(q):
        x, y = map(int, input().split())
        ix = bisect_left(a, x)
        if ix == n:
            print(x + y - 1)
            continue
        # 番号的に何個差があるか
        counter = a[-1] - x + 1 - ((n - 1) - ix + 1)
        if counter < y:
            print(a[-1] + y - counter)
            continue
        l, r = ix - 1, n
        while r - l > 1:
            mid = (r + l) // 2
            # 何個差があるかを、数の差と何要素間にあるかで図る
            can = (a[mid] - x + 1) - (mid - ix + 1)
            if can >= y:
                r = mid
            else:
                l = mid
        # 最大値に収まる
        elements_num = r - ix
        # print("[DEBUG] a[l], l, ix, element_num: ", a[r], r, ix, elements_num)
        print(x + (y - 1) + elements_num)

    return


if __name__ == "__main__":
    main()
