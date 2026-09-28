def main():
    N = int(input())
    A = list(map(int, input().split()))
    counter = sum(A[i - 1] < A[i] and A[i + 1] < A[i] for i in range(1, N - 1))
    print(counter)
    return


if __name__ == "__main__":
    main()
