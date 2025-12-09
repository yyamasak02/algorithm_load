from collections import deque


def main():
    n = int(input())
    visited = [False] * n
    costs = [float("inf")] * n
    d = {}
    for _ in range(n - 1):
        a, b, c = map(int, input().split())
        a -= 1
        b -= 1
        if a not in d:
            d[a] = {}
        if b not in d:
            d[b] = {}
        d[a][b] = c
        d[b][a] = c
    deq: deque = deque()
    for key, value in d[0].items():
        deq.append((0, key, 0))
    visited[0] = True
    costs[0] = 0
    while deq:
        pair = deq.popleft()

    return


if __name__ == "__main__":
    main()
