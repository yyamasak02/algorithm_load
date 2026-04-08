def main():
    N, X = map(int, input().split())
    A = list(map(int, input().split()))
    for i in range(N):
        if A[i] < X:
            print(1)
            X = A[i]
        else:
            print(0)
    return


if __name__ == "__main__":
    main()
