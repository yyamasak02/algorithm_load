def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    pattern_1 = [0] * N
    pattern_2 = [0] * N
    # counter = 0
    if A[0] != 0:
        pattern_1[0] += 1
    if A[0] != 1:
        pattern_2[0] += 1
    for i in range(1, N):
        if (A[i - 1] + pattern_1[i - 1] + A[i] + pattern_1[i]) % M != B[i - 1]:
            pattern_1[i] += 1
        if (A[i - 1] + pattern_2[i - 1] + A[i] + pattern_2[i]) % M != B[i - 1]:
            pattern_2[i] += 1
    result = min(sum(pattern_1), sum(pattern_2))
    print(result)
    return


if __name__ == "__main__":
    main()
