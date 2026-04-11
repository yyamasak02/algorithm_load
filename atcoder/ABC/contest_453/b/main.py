def main():
    T, X = map(int, input().split())
    A = list(map(int, input().split()))
    result = []
    for i in range(T + 1):
        if len(result) == 0:
            print(0, A[0])
            result.append(A[0])
        else:
            if abs(result[-1] - A[i]) >= X:
                print(i, A[i])
                result.append(A[i])
    return


if __name__ == "__main__":
    main()
