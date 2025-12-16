from bisect import bisect_right, bisect_left


def main():
    plus = []
    minus = []
    n, t = map(int, input().split())
    s = input()
    ll = list(map(int, input().split()))
    for i in range(n):
        if s[i] == "0":
            minus.append(ll[i])
        else:
            plus.append(ll[i])
    minus.sort()
    plus.sort()
    result = 0
    for c in plus:
        tmp = 2 * t + c
        index = bisect_right(minus, tmp)
        result += index - bisect_left(minus, c)
    print(result)
    return


if __name__ == "__main__":
    main()
