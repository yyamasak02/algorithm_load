import sys
import heapq


def main():
    input = sys.stdin.readline
    t = int(input())
    for _ in range(t):
        n, k, x = map(int, input().split())
        a = list(map(int, input().split()))
        d = {}
        b = []
        for c in a:
            if d.get(c) is None:
                d[c] = 0
            d[c] += 1
        for key, v in d.items():
            heapq.heappush(b, (-key, v))
        while k:
            key, v = heapq.heappop(b)
            if k <= v:
                heapq.heappush(b, (key / 2, 2 * k))
                heapq.heappush
                k = 0
                break
            break


if __name__ == "__main__":
    main()
