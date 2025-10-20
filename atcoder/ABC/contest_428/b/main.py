def main():
    n, k = map(int, input().split())
    s = input()
    d = {}
    for i in range(n - k + 1):
        tmp = s[i : i + k]
        if tmp not in d:
            d[tmp] = 0
        d[tmp] += 1
    ans = []
    res = max(d.values())
    for key, v in d.items():
        if res == v:
            ans.append(key)
    # print(d)
    ans.sort()
    print(res)
    print(*ans)
    return


if __name__ == "__main__":
    main()
