def main():
    n = int(input())
    a = []
    min_v = 0
    max_v = 0
    result = [-1] * n
    for i in range(n):
        l, r = map(int, input().split())
        min_v += l
        max_v += r
        a.append((l, r))
        result[i] = l

    def inner_target_value(a1, a2, v):
        return a1 <= v and a2 >= v

    if not inner_target_value(min_v, max_v, 0):
        print("No")
    else:
        print("Yes")
        sig_x = sum(result)
        for i in range(n):
            d = min(a[i][1] - a[i][0], -sig_x)
            sig_x += d
            result[i] += d
        print(*result)
    return


if __name__ == "__main__":
    main()
