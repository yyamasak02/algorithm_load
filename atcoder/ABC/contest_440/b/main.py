def main():
    n = int(input())
    a = list(map(int, input().split()))
    k = []
    for i in range(n):
        k.append((i, a[i]))
    k.sort(key=lambda x: x[1])
    print(f"{k[0][0] + 1} {k[1][0] + 1} {k[2][0] + 1}")
    return


if __name__ == "__main__":
    main()
