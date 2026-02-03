from bisect import bisect_left


def main():
    N, Q = map(int, input().split())
    a = sorted(list(map(int, input().split())))
    col = [0]
    for c in a:
        col.append(col[-1] + c)

    for _ in range(Q):
        b = int(input())
        index = bisect_left(a, b)
        if index == N:
            print(-1)
        else:
            print(col[index] + (N - index) * (b - 1) + 1)
    return


if __name__ == "__main__":
    main()
