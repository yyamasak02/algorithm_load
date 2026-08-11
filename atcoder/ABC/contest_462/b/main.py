def main():
    N = int(input())
    target = [[] for _ in range(N + 1)]
    for i in range(N):
        A = list(map(int, input().split()))
        K, A = A[0], A[1::]
        for j in range(K):
            target[A[j]].append(i + 1)
    for i in range(N):
        result = sorted(target[i + 1])
        print(len(result), *result)
    return


if __name__ == "__main__":
    main()
