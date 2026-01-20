def main():
    n, q = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    result = 0
    for i in range(n):
        result += min(a[i], b[i])
    for _ in range(q):
        query = input().split()
        x, v = int(query[1]), int(query[2])
        result -= min(a[x - 1], b[x - 1])
        if query[0] == "A":
            a[x - 1] = v
        else:
            b[x - 1] = v
        result += min(a[x - 1], b[x - 1])
        print(result)
    return


if __name__ == "__main__":
    main()
