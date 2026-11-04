def main():
    N, M = map(int, input().split())
    S_N = [input() for _ in range(N)]
    votes = [0] * N
    T_N = [input() for _ in range(M)]

    for t in T_N:
        target_index = -1
        nearly_count = 0
        for i in range(N):
            if S_N[i] == t:
                votes[i] += 1
                target_index = -1
                break
            if len(t) == len(S_N[i]):
                diff_num = sum(t[j] != S_N[i][j] for j in range(len(t)))
                if diff_num == 1:
                    target_index = i
                    nearly_count += 1
        if target_index != -1 and nearly_count == 1:
            votes[target_index] += 1
    for vote in votes:
        print(vote)
    return


if __name__ == "__main__":
    main()
