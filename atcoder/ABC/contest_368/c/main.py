import sys


def main():
    input = sys.stdin.readline
    n = int(input())
    a = list(map(int, input().split()))
    t = 0
    minus = (1, 1, 3, 1, 1, 3)
    for c in a:
        if c <= 0:
            continue
        div = c // 5
        mod = c % 5
        t += div * 3
        mod_c = t % 3
        while mod > 0:
            t += 1
            mod -= minus[mod_c]
            mod_c += 1
    print(t)
    return


if __name__ == "__main__":
    main()
