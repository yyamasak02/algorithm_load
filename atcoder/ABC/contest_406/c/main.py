def get_run_length_encoding(P: list[int]) -> list[tuple[str, int]]:
    run_length_encoding: list[tuple[str, int]] = []
    dir_flag: str = ""
    count: int = 0
    for i in range(1, N):
        if P[i] > P[i - 1]:
            if (dir_flag == ">"):
                run_length_encoding.append((dir_flag, count))
                count = 0
            dir_flag = "<"
            count += 1
        else:
            if (dir_flag == "<"):
                run_length_encoding.append((dir_flag, count))
                count = 0
            dir_flag = ">"
            count += 1
    run_length_encoding.append((dir_flag, count))
    return run_length_encoding

if __name__ == "__main__":
    N: int = int(input())
    P: list[int] = list(map(int, input().split()))
    run_length_encoding: list[tuple[str, int]] = get_run_length_encoding(P)
    ans: int = 0
    if len(run_length_encoding) <= 2:
        print(0)
        exit(0)
    for i in range(1, len(run_length_encoding) - 1):
        if run_length_encoding[i][0] == ">":
            ans += run_length_encoding[i-1][1] * run_length_encoding[i+1][1]
    print(ans)
