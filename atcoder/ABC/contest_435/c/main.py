def main():
    n = int(input())
    a = list(map(int, input().split()))
    a.insert(0, 0)
    ranger = a[1]
    for i in range(1, n):
        if a[i] + i - 1 >= ranger:
            ranger = min(a[i] + i - 1, n)
        if ranger < i + 1:
            break
    print(ranger)
    return


if __name__ == "__main__":
    main()
