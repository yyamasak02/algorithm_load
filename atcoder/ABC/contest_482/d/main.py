import sys


def main():
    input = sys.stdin.readline
    N = int(input())
    X = list(map(int, input().split()))
    ans = [0] * N
    for k in range(N):
        best = float("inf")
        if k + 1 < N:
            best = min(best, max((X[-1] - X[k]) // 2, (X[k + 1] - X[0]) // 2))
        if k >= 1:
            best = min(best, max((X[k] - X[0]) // 2, (X[-1] - X[k - 1]) // 2))
        ans[k] = best if N > 1 else 0
    print("\n".join(map(str, ans)))


if __name__ == "__main__":
    main()
