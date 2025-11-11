from sortedcontainers import SortedList


def main():
    h, w, q = map(int, input().split())
    g1 = [SortedList(range(w)) for _ in range(h)]
    g2 = [SortedList(range(h)) for _ in range(w)]

    def erase(r: int, c: int):
        if c in g1[r]:
            g1[r].remove(c)
        if r in g2[c]:
            g2[c].remove(r)

    for _ in range(q):
        R, C = map(int, input().split())
        R -= 1
        C -= 1

        if C in g1[R]:
            erase(R, C)
            continue

        # 上
        it = g2[C].bisect_left(R)
        if it > 0:
            erase(g2[C][it - 1], C)

        # 下
        it = g2[C].bisect_left(R)
        if it < len(g2[C]):
            erase(g2[C][it], C)

        # 左
        it = g1[R].bisect_left(C)
        if it > 0:
            erase(R, g1[R][it - 1])

        # 右
        it = g1[R].bisect_left(C)
        if it < len(g1[R]):
            erase(R, g1[R][it])
    ans = 0
    for i in range(h):
        ans += len(g1[i])
    print(ans)
    return


if __name__ == "__main__":
    main()
