def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    sorted_a = sorted(A)
    left, right = -1, -1
    for i in range(N):
        if A[i] != sorted_a[i]:
            left = i
            break
    for i in reversed(range(N)):
        if A[i] != sorted_a[i]:
            right = i
            break
    result = "Yes" if right - left < K else "No"
    print(result)
    return


if __name__ == "__main__":
    main()
