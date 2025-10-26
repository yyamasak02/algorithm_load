def main():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    gokei = sum(a)
    sa = gokei - m
    flag = False
    for c in a:
        if sa == c:
            flag = True
            break
    if flag is True:
        print("Yes")
    else:
        print("No")
    return


if __name__ == "__main__":
    main()
