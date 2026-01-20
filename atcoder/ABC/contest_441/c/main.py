def main():
    n, k, x = map(int, input().split())
    a = sorted(list(map(int, input().split())), reverse=True)
    expect_min = 0
    least_num = -1
    for i in range(n - k, n):
        expect_min += a[i]
        if expect_min >= x and least_num == -1:
            least_num = i + 1
    if least_num == -1:
        print("-1")
    else:
        print(least_num)
    return


if __name__ == "__main__":
    main()
