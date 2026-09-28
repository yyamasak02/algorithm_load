def main():
    def calc_permutation_count(num: int) -> int:
        result = 1
        for i in range(1, num + 1):
            result *= i
        return result

    N = int(input())
    P = list(map(int, input().split()))
    Q = list(map(int, input().split()))
    p_rank, q_rank = 0, 0
    visited_p = [False] * (N + 1)
    visited_q = [False] * (N + 1)
    for i in range(N):
        visited_p[P[i]] = True
        visited_q[Q[i]] = True
        valid_p = sum(visited_p[j] is False for j in range(1, P[i]))
        valid_q = sum(visited_q[j] is False for j in range(1, Q[i]))
        p_rank += calc_permutation_count(N - i - 1) * (valid_p)
        q_rank += calc_permutation_count(N - i - 1) * (valid_q)
    print(max(0, q_rank - p_rank - 1))
    return


if __name__ == "__main__":
    main()
