def main():
    N, M = map(int, input().split())
    d = {i: set() for i in range(1, N + 1)}
    for _ in range(M):
        a, b = map(int, input().split())
        d[a].add(b)
        d[b].add(a)
    result = [0] * (N + 1)
    for i in range(1, N + 1):
        size = N - len(d[i]) - 1
        result[i] = ((size) * (size - 1) * (size - 2)) // 6
    print(*result[1::])
    return


if __name__ == "__main__":
    main()
