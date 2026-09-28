import sys


def main():
    input = sys.stdin.readline  # sourcery skip: avoid-builtin-shadow
    N, Q = map(int, input().split())
    P = list(map(int, input().split()))
    reverse = [0] * N
    for i in range(N):
        reverse[P[i] - 1] = i + 1
    # print(P, reverse)
    for _ in range(Q):
        query = tuple(map(int, input().split()))
        if query[0] == 1:
            x, y = query[1] - 1, query[2] - 1
            P[x], P[y] = P[y], P[x]
            reverse[P[x] - 1], reverse[P[y] - 1] = reverse[P[y] - 1], reverse[P[x] - 1]
        else:
            P, reverse = reverse, P
    print(*P)
    return


if __name__ == "__main__":
    main()
