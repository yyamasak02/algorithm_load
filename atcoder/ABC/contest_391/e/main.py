def f(ll, r):
    if ll + 1 == r:
        return A[ll], 1
    m1 = (2 * ll + r) // 3
    m2 = (ll + 2 * r) // 3
    val1, cnt1 = f(ll, m1)
    val2, cnt2 = f(m1, m2)
    val3, cnt3 = f(m2, r)

    if val1 == val2 == val3:
        return val1, cnt1 + cnt2 + cnt3 - max(cnt1, cnt2, cnt3)
    elif val1 == val2:
        return val1, min(cnt1, cnt2)
    elif val1 == val3:
        return val1, min(cnt1, cnt3)
    elif val2 == val3:
        return val2, min(cnt2, cnt3)


if __name__ == "__main__":
    global A, N
    N = int(input())
    A = input().rstrip()
    print(f(0, 3**N)[1])
