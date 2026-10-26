def main():
    N, Q = map(int, input().split())
    P = list(map(int, input().split()))
    ans = [0] * (N + 1)
    for i in range(N):
        ans[P[i]] = i + 1
    for i in range(Q):
        ans[int(input())] = N + i + 1
    array = [
        t1
        for t1, t2 in sorted(
            ((i + 1, ans[i + 1]) for i in range(N)), key=lambda x: x[1]
        )
    ]
    print(*array)
    return


if __name__ == "__main__":
    main()
