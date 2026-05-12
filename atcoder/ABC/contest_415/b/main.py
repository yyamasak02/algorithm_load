def main():
    S = input()
    first = -1
    for i in range(len(S)):
        if S[i] == "#" and first != -1:
            print(f"{first + 1},{i + 1}")
            first = -1
        elif S[i] == "#":
            first = i
    return


if __name__ == "__main__":
    main()
