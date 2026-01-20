import math


def main():
    n = int(input())
    cnt = [0] * (n + 1)

    limit = int(math.isqrt(n))
    for x in range(1, limit + 1):
        xx = x * x
        for y in range(x + 1, int(math.isqrt(n - xx)) + 1):
            cnt[xx + y * y] += 1
    result = [i for i in range(n + 1) if cnt[i] == 1]
    print(len(result))
    print(*result)
    return


if __name__ == "__main__":
    main()
