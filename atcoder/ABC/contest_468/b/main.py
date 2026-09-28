def main():
    M, D = map(int, input().split())
    S = input()
    counter = 0
    for i in range(M):
        if S[i] == "G":
            continue

        def check(right_edge, left_edge):
            for j in range(i, right_edge):
                if S[j] == "G":
                    return False
            for j in range(i, left_edge, -1):
                if S[j] == "G":
                    return False
            return True

        right_edge = min(i + D + 1, M)
        left_edge = max(-1, i - D - 1)
        if check(right_edge=right_edge, left_edge=left_edge) is True:
            counter += 1
    print(counter)
    return


if __name__ == "__main__":
    main()
