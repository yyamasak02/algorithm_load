def main():
    N, M, K = map(int, input().split())
    a_list = list(map(int, input().split()))
    is_ate = [False] * N
    total_cal = 0
    for i in range(N):
        if i >= M and is_ate[i - M] is True:
            total_cal -= a_list[i - M]
        if total_cal + a_list[i] <= K:
            total_cal += a_list[i]
            is_ate[i] = True
            print("Yes")
        else:
            print("No")
    return


if __name__ == "__main__":
    main()
