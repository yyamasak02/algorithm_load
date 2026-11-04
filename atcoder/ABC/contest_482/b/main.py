def main():
    masu = [input() for _ in range(5)]
    transposed = [list(row) for row in zip(*masu)]
    min_reach = 5
    left_cross, right_cross = 0, 0
    for i in range(5):
        if masu[i][i] == "o":
            left_cross += 1
        if masu[i][-i - 1] == "o":
            right_cross += 1
        min_reach = min(min_reach, 5 - masu[i].count("o"), 5 - transposed[i].count("o"))

    min_reach = min(min_reach, 5 - left_cross, 5 - right_cross)
    print(min_reach)
    return


if __name__ == "__main__":
    main()
