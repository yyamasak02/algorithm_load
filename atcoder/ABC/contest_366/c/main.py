import sys


def main():
    input = sys.stdin.readline
    x_counts = {}
    q = int(input())
    ans = 0
    for _ in range(q):
        query = tuple(map(int, input().split()))
        if query[0] == 1:
            if query[1] not in x_counts:
                x_counts[query[1]] = 0
            x_counts[query[1]] += 1
            if x_counts[query[1]] == 1:
                ans += 1
        elif query[0] == 2:
            x_counts[query[1]] -= 1
            if x_counts[query[1]] == 0:
                ans -= 1
        else:
            print(ans)
    return


if __name__ == "__main__":
    main()
