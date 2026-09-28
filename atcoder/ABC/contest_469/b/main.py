def main():
    N = int(input())
    S = input()
    counter = 0
    for i in range(N):
        if i != 0 and S[i - 1] == "o":
            continue
        if i != N - 1 and S[i + 1] == "o":
            continue
        if S[i] == "o":
            continue
        counter += 1
    print(counter)
    return


if __name__ == "__main__":
    main()
