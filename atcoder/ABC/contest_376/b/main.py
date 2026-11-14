def solve(target, obstacle, acheive, size):
    if target == obstacle:
        return 0
    if target > obstacle and obstacle > acheive:
        pass

    return


if __name__ == "__main__":
    n, q = map(int, input().split())
    l = 0
    r = 1
    ans = 0
    for _ in range(q):
        h, t = map(str, input().split())
        t = int(t) - 1
        if h == "L":
            ans += solve(l, r, t, n)
            l = t
        else:
            ans += solve(r, l, t, n)
            r = t
    print(ans)
