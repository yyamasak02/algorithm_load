def main():
    N, M = map(int, input().split())
    A = sorted(list(map(int, input().split())))
    B = sorted(list(map(int, input().split())))
    ia, ib, result = 0, 0, 0
    while ia < len(A) and ib < len(B):
        capacity = A[ia] * 2
        if capacity >= B[ib]:
            result += 1
            ib += 1
        ia += 1
    print(result)
    return


if __name__ == "__main__":
    main()
