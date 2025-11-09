import sys
from itertools import permutations

"""
    <方針>
    ・変換後の頂点の置き方について、変換前のグラフとすべての対応関係でコストを計算し、最小値を採用する
"""


def eval(
    hNodes: list[set], gNodes: list[set], p: tuple, n: int, costs: list[list[int]]
) -> int:
    totalValue = 0
    for i in range(n):
        for j in range(i + 1, n):
            g_has_edge = j in gNodes[i]
            v_h1 = p[i]
            v_h2 = p[j]
            h_has_edge = v_h2 in hNodes[v_h1]
            if g_has_edge != h_has_edge:
                totalValue += costs[v_h1][v_h2]
    return totalValue


def main():
    input = sys.stdin.readline
    n = int(input())

    # mg
    mg = int(input())
    gNodes: list[set] = [set() for _ in range(n)]
    for _ in range(mg):
        u, v = map(int, input().split())
        u -= 1
        v -= 1
        gNodes[u].add(v)
        gNodes[v].add(u)

    # mh
    mh = int(input())
    hNodes: list[set] = [set() for _ in range(n)]
    for _ in range(mh):
        u, v = map(int, input().split())
        u -= 1
        v -= 1
        hNodes[u].add(v)
        hNodes[v].add(u)
    # costs
    costs: list[list[int]] = [[0] * n for _ in range(n)]
    for i in range(n):
        q = list(map(int, input().split()))
        for j, c in enumerate(q):
            costs[i][j + i + 1] = c
            costs[j + i + 1][i] = c
    uniquePermutations: set[tuple] = permutations(range(n))
    ans = 10**10
    for p in uniquePermutations:
        ans = min(ans, eval(hNodes=hNodes, gNodes=gNodes, p=p, n=n, costs=costs))
    print(ans)
    return


if __name__ == "__main__":
    main()
