from bisect import bisect_left


def main():
    n, m = map(int, input().split())
    a = sorted(list(map(int, input().split())))
    b = sorted(list(map(int, input().split())))
    start_index = 0
    result = 0
    for i in range(m):
        v = b[i]
        index = bisect_left(a, v, start_index)
        if index >= n:
            result = -1
            break
        result += a[index]
        start_index = index + 1
    print(result)
    return


if __name__ == "__main__":
    main()
