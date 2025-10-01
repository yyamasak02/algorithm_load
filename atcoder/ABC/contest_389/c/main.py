import sys
from collections import deque


def main():
    input = sys.stdin.readline
    q: int = int(input())
    a: deque[int] = deque()
    minus: int = 0
    for _ in range(q):
        query = tuple(map(int, input().split()))
        if query[0] == 1:
            if len(a) == 0:
                a.append((query[1], query[1]))
            else:
                a.append((query[1], a[-1][1] + query[1]))
        elif query[0] == 2:
            tmp = a.popleft()
            minus += tmp[0]
        else:
            print(a[query[1] - 1][1] - a[query[1] - 1][0] - minus)
    return


if __name__ == "__main__":
    main()
