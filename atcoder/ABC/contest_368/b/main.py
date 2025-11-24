def main():
    n = int(input())
    a = sorted(list(map(int, input().split())), reverse=True)
    c = 0
    while True:
        if a[1] <= 0:
            break
        c += 1
        a[0] -= 1
        a[1] -= 1
        a.sort(reverse=True)
    print(c)
    return


if __name__ == "__main__":
    main()
