import math


def main():
    x1, x2, x3 = map(int, input().split())
    tt = math.factorial(x1 + x2 + x3)
    tx1 = math.factorial(x1)
    tx2 = math.factorial(x2)
    tx3 = math.factorial(x3)
    tt %= tx1
    tt %= tx2
    tt %= tx3
    tt %= 998244353

    return


if __name__ == "__main__":
    main()
