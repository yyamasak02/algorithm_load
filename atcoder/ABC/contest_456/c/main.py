def main():
    S = input()
    size = len(S)

    result = size
    prev, pi = None, 0
    for i in range(size):
        if S[i] == prev:
            result += (i - pi) * (i - pi - 1) // 2
            # print(f"{pi} ~ {i}")
            pi = i
        prev = S[i]
    # print(f"{pi} ~ {i}")
    result += (i - pi + 1) * (i - pi) // 2
    print(result)
    return


if __name__ == "__main__":
    main()
