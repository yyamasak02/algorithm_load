def main():
    t = int(input())
    for _ in range(t):
        n = int(input())
        a = []
        total_w = 0
        total_p = 0
        for _ in range(n):
            w, p = map(int, input().split())
            a.append((w, p, p + w))
            total_w += w
        index = 0
        a.sort(reverse=True, key=lambda x: (x[2], x[0]))
        # from pprint import pprint
        # pprint(a)
        while (total_w > total_p) and (index < n):
            total_w -= a[index][0]
            total_p += a[index][1]
            index += 1
        print(n - index)
    return


if __name__ == "__main__":
    main()
