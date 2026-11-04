def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    counter = sum(
        1
        for i in range(N - 1)
        if (A[i] < K <= A[i + 1]) or (A[i + 1] <= K < A[i]) or (i == 0 and A[i] == K)
    )
    print(counter)
    return


if __name__ == "__main__":
    main()
