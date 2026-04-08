from collections import deque


def main():
    def calcMin(x, ai) -> int:
        numbers = [0]
        bin_ai = bin(ai)[2:]
        size = len(bin_ai)
        result = None
        for i in range(size):
            if bin_ai[-(i + 1)] == "1":
                number = 2**i
                tmp = []
                for num in numbers:
                    if number + num >= x:
                        result = number + num
                        break
                    tmp.append(number + num)
                if result is not None:
                    break
                numbers.extend(tmp)
        if result is None:
            return -1
        return result

    N, M = map(int, input().split())
    d = {key: {} for key in range(1, N + 1)}
    for i in range(M):
        u, v, a = map(int, input().split())
        d[u][v] = a
        d[v][u] = a
    queue: deque[tuple[int, int]] = deque()
    results = [[float("inf"), -1] for _ in range(N + 1)]
    results[1][0] = 1
    results[1][1] = 1
    queue.append((1, 1))
    while queue:
        ctx, x = queue.popleft()
        if ctx == N:
            continue
        for nxt in d[ctx].keys():
            ai = d[ctx][nxt]
            minValue = results[nxt][0]
            maxValue = results[nxt][1]
            if x <= ai:
                if maxValue < ai:
                    results[nxt][1] = ai
                    queue.append((nxt, ai))
                if ai < minValue:
                    num = calcMin(x, ai)
                    if num != -1:
                        results[nxt][0] = num
                        queue.append((nxt, num))
    minV, maxV = (
        -1 if results[-1][0] == float("inf") else results[-1][0],
        results[-1][1],
    )
    print(minV, maxV)
    return


if __name__ == "__main__":
    main()
