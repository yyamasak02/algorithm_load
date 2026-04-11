def main():
    N = int(input())
    S = input()
    a = []
    i = 0
    if S[0] == "o":
        for i in range(N):
            if S[i] != "o":
                break
    if S[i] != "o":
        for j in range(i, N):
            a.append(S[j])
    print("".join(a))
    return


if __name__ == "__main__":
    main()
