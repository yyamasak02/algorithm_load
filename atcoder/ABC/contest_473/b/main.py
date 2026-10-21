def main():
    _ = int(input())
    A = list(map(int, input().split()))
    d = {}
    for a in A:
        if a not in d:
            d[a] = 0
        d[a] += 1
    total = sum(key for key, value in d.items() if value % 2 == 1)
    print(total)
    return


if __name__ == "__main__":
    main()
