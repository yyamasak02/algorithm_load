import sys
from collections import Counter


def main():
    input = sys.stdin.readline
    N, Q = map(int, input().split())
    result_sets = [[Counter(), Counter()] for _ in range(N + 2)]
    for _ in range(Q):
        L, R, X = map(int, input().split())
        result_sets[L][0][X] += 1
        result_sets[R + 1][1][X] += 1
    ans = Counter()
    result = []
    # print(result_sets)
    for i in range(N):
        for x, c in result_sets[i + 1][1].items():
            ans[x] -= c
            if ans[x] <= 0:
                del ans[x]
        for x, c in result_sets[i + 1][0].items():
            ans[x] += c
        # print(ans)
        result.append(len(ans))
    # print(result_sets)
    print(*result)
    # print("3 4 5 6 6 6 7 7 8 8 9 8 8 9 9 10 9 8 7 7 7 6 7 5 3 2 2 2 2 2")
    return


if __name__ == "__main__":
    main()
