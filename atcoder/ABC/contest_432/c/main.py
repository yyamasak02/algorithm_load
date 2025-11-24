def main():
    n, x, y = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort()

    delta = y - x
    min_v = a[0] * x
    max_v = a[0] * y
    r = min_v % delta
    error = False
    result = 0
    for v in a:
        tmp = v * x
        if tmp % delta != r or tmp > max_v:
            error = True
            break
        result += (max_v - tmp) // delta
    if error is True:
        print(-1)
    else:
        print(result)
    return


if __name__ == "__main__":
    main()
