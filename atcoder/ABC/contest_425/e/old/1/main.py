import sys


def main():
    input = sys.stdin.readline
    t, m = map(int, input().split())
    K = 5001
    kl = [[0] * K for _ in range(K)]
    kl[0][0] = 1
    for i in range(1, K):
        kl[i][0] = 1
        for j in range(1, i + 1):
            kl[i][j] = (kl[i - 1][j - 1] + kl[i - 1][j]) % m

    for _ in range(t):
        _ = int(input())
        c = list(map(int, input().split()))
        ans = 1
        s = 0
        for i in c:
            s += i
            ans *= kl[s][i]
            ans %= m
        print(ans % m)
    return


if __name__ == "__main__":
    main()
