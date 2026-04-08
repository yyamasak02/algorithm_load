def main():
    N, T = map(int, input().split())
    if N == 0:
        print(T)
        exit(0)

    A = list(map(int, input().split()))
    total, last_seen, is_seen = 0, -100, True
    for i in range(N):
        if A[i] - last_seen >= 100:
            total += A[i] - last_seen - 100
            last_seen = A[i]
    # print(A[N-1], last_seen, T)
    total += max(T - last_seen - 100, 0)
    print(total)
    return


if __name__ == "__main__":
    main()
