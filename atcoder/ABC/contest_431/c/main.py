def main():
    n, m, k = map(int, input().split())
    hList = sorted(list(map(int, input().split())))
    wList = sorted(list(map(int, input().split())))
    dh = 0
    dw = 0
    c = 0
    while True:
        if wList[dw] >= hList[dh]:
            c += 1
            dw += 1
            dh += 1
        else:
            dw += 1
        if dw >= m or dh >= n or c >= k:
            break
    ans = "Yes" if c >= k else "No"
    print(ans)

    return


if __name__ == "__main__":
    main()
