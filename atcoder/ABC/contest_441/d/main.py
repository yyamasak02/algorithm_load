from collections import deque


def main():
    N, M, L, S, T = map(int, input().split())
    d = {k: set() for k in range(1, N + 1)}
    costs_map = {k: {} for k in range(1, N + 1)}
    costs = [[] for _ in range(N + 1)]
    for _ in range(M):
        u, v, c = map(int, input().split())
        d[u].add(v)
        if v not in costs_map[u]:
            costs_map[u][v] = []
        costs_map[u][v].append(c)
    q: deque = deque()
    q.append((1, 0, 0))
    destinations = set()
    while q:
        cpos, step, current_cost = q.popleft()
        for nxt in d[cpos]:
            nxt_costs = []
            for target_cost in costs_map[cpos][nxt]:
                nxt_cost = current_cost + target_cost
                if T >= nxt_cost and step + 1 <= L:
                    q.append((nxt, step + 1, nxt_cost))
                if step + 1 == L and nxt_cost >= S and T >= nxt_cost:
                    destinations.add(nxt)
    destinations = sorted(list(destinations))
    print(*destinations)
    return


if __name__ == "__main__":
    main()
