def main():
    n, k = map(int, input().split())
    if k % (2**n) == 0:
        div = k // (2**n)
        s = (str(div) + " ") * ((2**n) - 1)
        s = s + str(div)
        print(0)
        print(s)
    else:
        ans = [k]
        for i in range(n):
            nxt = []
            for c in ans:
                nxt.append(c // 2)
                nxt.append(c - c // 2)
            ans = nxt
        print(1)
        print(*ans)
    return


if __name__ == "__main__":
    main()
