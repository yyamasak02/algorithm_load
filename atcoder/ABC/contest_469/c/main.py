def main():
    N = int(input())
    S = input()
    answers = [0] * (N + 1)
    nones = [i for i in range(N) if S[i] == "x"]
    size = len(nones)
    ok_count, left_index = 0, 0
    for i in range(1, N + 1):
        if S[i - 1] == "o":
            ok_count += 1
        else:
            left_index += 1

        if ok_count + left_index > size:
            answers[i] = N
        else:
            answers[i] = nones[ok_count + left_index - 1] + 1
    print(*answers[1::], sep="\n")
    return


if __name__ == "__main__":
    main()
