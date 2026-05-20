from itertools import combinations


def main():
    N, M, K = map(int, input().split())
    d = {}
    for _ in range(M):
        row = input().split()
        C, A, R = int(row[0]), sorted(list(map(int, row[1:-1]))), row[-1]
        target_combs = combinations(A, K)
        for comb in target_combs:
            if comb not in d:
                d[comb] = 0
            if R == "o" and d[comb] != -1:
                d[comb] += 1
            else:
                d[comb] = -1
    max_value_count = list(d.values()).count(max(0, max(d.values())))
    print(max_value_count)
    return


if __name__ == "__main__":
    main()
