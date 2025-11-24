def main():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    new_a = []
    for i in range(k, 0, -1):
        new_a.append(a[-i])
    for i in range(n - k):
        new_a.append(a[i])
    print(*new_a)
    return


if __name__ == "__main__":
    main()
