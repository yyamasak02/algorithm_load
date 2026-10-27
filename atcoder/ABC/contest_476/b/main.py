def main():
    N = int(input())
    S = input()
    T = input()
    created_string = ""
    for i in range(N):
        if T[i] == "*":
            created_string = created_string + S[i]
        else:
            created_string = created_string + T[i]
    if S == created_string:
        print("Yes")
    else:
        print("No")
    return


if __name__ == "__main__":
    main()
