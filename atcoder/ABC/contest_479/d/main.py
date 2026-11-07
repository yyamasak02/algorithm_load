import sys


def main():
    input = sys.stdin.readline
    N, Q = map(int, input().split())
    L_N = list(map(int, input().split()))
    L_N.insert(0, 0)
    L_N.insert(0, 0)
    tentative_min_l, tentative_min_r = [], []
    for i in reversed(range(N + 1)):
        if not tentative_min_l:
            tentative_min_l.append(i)
        elif L_N[tentative_min_l[-1]] < L_N[i]:
            tentative_min_l.append(tentative_min_l[-1])
        else:
            tentative_min_l.append(i)
    tentative_min_l = list(reversed(tentative_min_l))
    R_N = list(map(int, input().split()))
    R_N.append(0)
    R_N.insert(0, 0)
    for i in range(N + 1):
        if not tentative_min_r or i == 1:
            tentative_min_r.append(i)
        elif R_N[tentative_min_r[-1]] < R_N[i]:
            tentative_min_r.append(tentative_min_r[-1])
        else:
            tentative_min_r.append(i)
    # print(*L_N, "\n", *R_N)
    # print(*tentative_min_l, "\n", *tentative_min_r)
    queries = [tuple(map(int, input().split())) for _ in range(Q)]
    for query in queries:
        if query[0] == 1:
            print(R_N[1])
        elif query[0] == N:
            print(L_N[N])
        else:
            if query[0] < query[1]:
                result = min(
                    R_N[query[0]], L_N[query[0]] + R_N[tentative_min_r[query[0] - 1]]
                )
            else:
                result = min(
                    L_N[query[0]], R_N[query[0]] + L_N[tentative_min_l[query[0] + 1]]
                )
            print(result)
    return


if __name__ == "__main__":
    main()
