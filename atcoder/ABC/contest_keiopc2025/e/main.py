def main():
    def checkSimpleDigit(n) -> int:
        for i in range(10):
            if n % 10**i != 0:
                return i

    def reverseNum(n, limit) -> int:
        result = 0
        str_n = str(n)
        size = len(str_n)
        for i in range(size - limit):
            result *= 10
            result += int(str_n[i])
        return result

    N, M = map(int, input().split())
    ans = 0
    for i in range(1, 10**N):
        if i % 10 == 0:
            digit = checkSimpleDigit(i)
            digit -= 1
            tmp = reverseNum(i, digit) ** M
        else:
            tmp = i**M
        ans += tmp
        ans %= 998244353
    print(ans)
    return


if __name__ == "__main__":
    main()
