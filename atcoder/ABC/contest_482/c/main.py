import sys
from bisect import bisect_left, bisect_right


def main():
    input = sys.stdin.readline
    H, W, N, Q = map(int, input().split())
    columns = []
    rows = []
    for _ in range(N):
        ri, ci = map(int, input().split())
        rows.append(ri)
        columns.append(ci)
    rows.sort()
    columns.sort()
    for _ in range(Q):
        query = tuple(map(int, input().split()))
        if query[0] == 1:
            lower_limit, upper_limit = (
                bisect_left(rows, query[1]),
                bisect_right(rows, query[2]),
            )
        else:
            lower_limit, upper_limit = (
                bisect_left(columns, query[1]),
                bisect_right(columns, query[2]),
            )
        print(upper_limit - lower_limit)
    return


if __name__ == "__main__":
    main()
