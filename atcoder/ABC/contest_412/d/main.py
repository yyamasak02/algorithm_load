from itertools import combinations


def is_valid_cycle(edge_subset, n) -> bool:
    tmp: list[int] = [0 for _ in range(n)]
    for edge in edge_subset:
        tmp[edge[0]] += 1
        tmp[edge[1]] += 1
    return all(x == 2 for x in tmp)

if __name__ == "__main__":
    n,m = map(int,input().split())
    d = set()
    for i in range(m):
        a,b = map(int,input().split())
        a -= 1
        b -= 1
        if a > b:
            a,b = b,a
        d.add((a,b))
    all_possible_edges = [(i, j) for i in range(n) for j in range(i + 1, n)]
    ans = 10**18
    for tmp in combinations(all_possible_edges, n):
        candidate_set = set(tmp)
        if is_valid_cycle(tmp, n):
            need_set = candidate_set - d
            remove_set = d - candidate_set
            ans = min(ans, len(need_set) + len(remove_set))
    print(ans)

