def main():
    n = int(input())
    a = list(map(int, input().split()))
    result = []
    ans = [0] * n
    for i in range(n - 2, -1, -1):
        while result and a[result[-1]] < a[i + 1]:
            result.pop()
        result.append(i + 1)
        ans[i] = len(result)
    print(*ans)
    return


if __name__ == "__main__":
    main()
