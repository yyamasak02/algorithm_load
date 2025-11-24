def main():
    n = int(input())
    a = list(map(int, input().split()))
    result = [-1] * n
    for i in range(n):
        for j in range(i, -1, -1):
            if a[i] < a[j]:
                result[i] = j + 1
                break
    for c in result:
        print(c)
    return


if __name__ == "__main__":
    main()
