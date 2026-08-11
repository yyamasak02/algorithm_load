def main():
    N = int(input())
    S = input()
    result = [0] * N
    L, R = 0, N - 1
    reverse_count = 0
    while N > 0:
        if S[N - 1] == "o":
            reverse_count += 1

        if reverse_count % 2 == 1:
            result[L] = N
            L += 1
        else:
            result[R] = N
            R -= 1
        N -= 1
    print(*result)
    return


if __name__ == "__main__":
    main()
