import sys


def main():
    input = sys.stdin.readline
    N, K = map(int, input().split())
    ans = []
    path = [0] * N

    def solve(n, k):
        if n == 1:
            path[0] = k
            ans.append(tuple(path))
            return
        tmp = k // n
        for num in range(tmp, -1, -1):
            path[n - 1] = num
            solve(n - 1, k - num * n)

    solve(N, K)
    print("\n".join(" ".join(map(str, e)) for e in sorted(ans)))
    return


if __name__ == "__main__":
    main()
