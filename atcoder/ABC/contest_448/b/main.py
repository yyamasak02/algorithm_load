def main():
    N, M = map(int, input().split())
    C = list(map(int, input().split()))
    D = [0] * M
    for _ in range(N):
        a, b = map(int, input().split())
        D[a - 1] += b
    result = 0
    for i in range(M):
        result += min(C[i], D[i])
    print(result)
    return


if __name__ == "__main__":
    main()
