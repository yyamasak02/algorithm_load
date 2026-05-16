def main():
    S = input()
    size = len(S)
    counter = 0
    for i in range(size):
        if S[i] == "C":
            left, right = max(0, i), max(0, size - (i + 1))
            counter += min(left, right)
            counter += 1
    print(counter)
    return


if __name__ == "__main__":
    main()
