def main():
    T = int(input())
    for _ in range(T):
        N = int(input())
        S = f"0{input()}"
        safety_visited = [False] * ((1 << N) + 1)
        safety_visited[0] = True
        for i in range(1 << N):
            if safety_visited[i] is False:
                continue
            for j in range(N):
                if i & (1 << j):
                    continue
                next_state = i | (1 << j)
                if S[next_state] == "0":
                    safety_visited[next_state] = True
        if safety_visited[(1 << N) - 1] is True:
            print("Yes")
        else:
            print("No")
    return


if __name__ == "__main__":
    main()
