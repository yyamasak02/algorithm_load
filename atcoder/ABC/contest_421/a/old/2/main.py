def main():
    n = int(input())
    d = {}
    for i in range(n):
        d[i + 1] = input()
    x, y = input().split()
    x = int(x)
    result = "Yes" if d[x] == y else "No"
    print(result)
    return


if __name__ == "__main__":
    main()
