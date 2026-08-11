def main():
    X, Y, L, R, A, B = map(int, input().split())
    if R <= A or B <= L:
        print((B - A) * Y)
    elif L <= A and B <= R:
        print((B - A) * X)
    elif L <= A and R <= B:
        fee_a = max(R - A, 0) * X
        fee_a += max(B - R, 0) * Y
        print(fee_a)
    elif A <= L and B <= R:
        fee_a = max(L - A, 0) * Y
        fee_a += max(B - L, 0) * X
        print(fee_a)
    elif A <= L and R <= B:
        fee_a = max(L - A, 0) * Y
        fee_a += max(R - L, 0) * X
        fee_a += max(B - R, 0) * Y
        print(fee_a)
    return


if __name__ == "__main__":
    main()
