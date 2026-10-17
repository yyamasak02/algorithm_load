import heapq
import sys


def main():
    input = sys.stdin.readline
    Q, V = map(int, input().split())
    queue = []
    heapq.heapify(queue)
    for _ in range(Q):
        query = tuple(map(int, input().split()))
        if query[0] == 1:
            t, w = query[1], query[2]
            heapq.heappush(queue, -w + t)
        else:
            if not queue:
                print(-1)
                continue
            target = heapq.heappop(queue)
            print(min(V, -target + query[1]))
    return


if __name__ == "__main__":
    main()
