from collections import deque


def main():
    N, M = map(int, input().split())
    visited = [False] * (N + 1)
    d = {0: set()}
    for _ in range(M):
        A, B = map(int, input().split())
        A -= 1
        B -= 1
        if A not in d:
            d[A] = set()
        d[A].add(B)
    deq = deque()
    deq.append(0)
    result = 0
    while deq:
        idx = deq.popleft()
        if visited[idx] is True:
            continue
        visited[idx] = True
        result += 1
        if idx in d:
            for target in d[idx]:
                if visited[target] is False:
                    deq.append(target)
    print(result)
    return


if __name__ == "__main__":
    main()
