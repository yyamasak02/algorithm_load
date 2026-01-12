import heapq


def main():
    N, K, X = map(int, input().split())
    a_list = sorted(list(map(int, input().split())), reverse=True)
    assign: list[int] = [0] * (N + 1)
    assign[0] = -a_list[0] * K
    assign[1] = K
    visited: set[tuple] = {tuple(assign)}
    q: list[tuple] = [tuple(assign)]
    for _ in range(X):
        assign = heapq.heappop(q)
        print(-assign[0])
        for i in range(1, N):
            if assign[i] == 0:
                continue
            ll = list(assign)
            ll[i] -= 1
            ll[i + 1] += 1
            ll[0] += a_list[i - 1] - a_list[i]
            if tuple(ll) in visited:
                continue
            heapq.heappush(q, tuple(ll))
            visited.add(tuple(ll))
    return


if __name__ == "__main__":
    main()
