import sys


def main():
    input = sys.stdin.readline
    N, Q = map(int, input().split())
    _ = list(map(int, input().split()))
    _ = list(map(int, input().split()))
    queries = []
    for _ in range(Q):
        s, t = map(int, input().split())
        queries.append((s, t))
    return


if __name__ == "__main__":
    main()
