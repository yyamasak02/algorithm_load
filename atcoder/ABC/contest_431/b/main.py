def main():
    x = int(input())
    n = int(input())
    w = list(map(int, input().split()))
    flag = [False] * n
    q = int(input())
    for _ in range(q):
        p = int(input())
        p -= 1
        if flag[p] is False:
            flag[p] = True
            x += w[p]
        else:
            flag[p] = False
            x -= w[p]
        print(x)
    return


if __name__ == "__main__":
    main()
