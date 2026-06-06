def main():
    N = int(input())
    result = [0] * (N + 1)
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    for i in range(1, N + 1):
        result[i] = A[i - 1]
    is_ok = True
    for i in range(1, N + 1):
        if result[B[i - 1]] != i:
            is_ok = False
            break
    if is_ok is True:
        print("Yes")
    else:
        print("No")
    return


if __name__ == "__main__":
    main()
