import sys


def main():
    input = sys.stdin.readline
    n, q = map(int, input().split())
    pc = [1 for i in range(n + 1)]
    o: int = 1
    for _ in range(q):
        x, y = map(int, input().split())
        result: int = 0
        for i in range(o, x + 1):
            result += pc[i]
            pc[y] += pc[i]
        o = x + 1 if o < x + 1 else o
        print(result)
    return


if __name__ == "__main__":
    main()
