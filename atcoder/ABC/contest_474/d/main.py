def main():
    N = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    result = [-1] * N
    diff = 0
    for i in range(N):
        diff += A[i] - B[i]
        result[i] = 1
    if diff <= 0:
        for i in range(N):
            if diff > 0:
                break
            if A[i] > B[i]:
                diff += (10**18 - 1) * (A[i] - B[i])
                result[i] = 10**18
        if diff > 0:
            print("Yes")
            print(*result)
        else:
            print("No")
    else:
        print("Yes")
        print(*result)

    return


if __name__ == "__main__":
    main()
