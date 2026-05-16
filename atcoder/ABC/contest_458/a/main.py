def main():
    S = input()
    N = int(input())
    size = len(S)
    S = S[N : size - N]
    print(S)
    return


if __name__ == "__main__":
    main()
