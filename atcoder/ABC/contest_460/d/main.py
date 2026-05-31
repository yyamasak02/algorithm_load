def main():
    H, W = map(int, input().split())
    # counter = 0
    field = []
    black_field = []
    for i in range(H):
        S = list(input())
        field.append(S)
    for i in range(H):
        for j in range(W):
            if field[i][j] == "#":
                black_field.append((i, j))

    return


if __name__ == "__main__":
    main()
