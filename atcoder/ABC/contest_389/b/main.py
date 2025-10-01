import sys


def main():
    input = sys.stdin.readline
    x: int = int(input())
    kl = [1]
    d = {1: 1}
    for i in range(2, 31):
        result = kl[-1] * i
        kl.append(result)
        d[result] = i
    print(d[x])
    return


if __name__ == "__main__":
    main()
